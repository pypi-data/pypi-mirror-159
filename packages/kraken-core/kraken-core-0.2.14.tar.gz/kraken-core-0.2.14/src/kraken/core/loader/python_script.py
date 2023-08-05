""" Implements a loader for Python scripts. These Python scripts have access to importing certain build context
related members from the :mod:`kraken.api` module; note that these members are only available when imported in
the context of a script executed by this loader and not otherwise. """

from __future__ import annotations

import contextlib
import sys
import types
from pathlib import Path
from typing import Any, Iterator

from kraken.core.project import Project

from . import ProjectLoader

KRAKEN_DIR = Path(".kraken")
DEFAULT_FILES = [
    Path(".kraken.py"),
    Path("kraken.build.py"),
    Path(".kraken.build.py"),
    KRAKEN_DIR / "kraken.py",
    KRAKEN_DIR / "kraken.build.py",
    KRAKEN_DIR / "build.py",
]
REQUIREMENTS_FILE = KRAKEN_DIR / "requirements.txt"


class PythonScriptProjectLoader(ProjectLoader):
    def detect_in_project_directory(self, project_dir: Path) -> Path | None:
        for file in (project_dir / f for f in DEFAULT_FILES):
            if file.is_file():
                return file
        return None

    def match_file(self, file: Path) -> bool | Path | None:
        return file.suffix == ".py"

    def load_script(self, file: Path, project: Project) -> None:
        requirements_file = project.directory / REQUIREMENTS_FILE
        if requirements_file.is_file():
            pip_args = [x for x in requirements_file.read_text().splitlines() if not x.startswith("#") and x.strip()]
            if pip_args:
                # TODO (@NiklasRosenstein): Can we gather the requirements of included subprojects as well?
                # TODO (@NiklasRosenstein): We only want to do the install/activate once for the root project.
                project.context.pyenv.install(pip_args)
                project.context.pyenv.activate()

        with inject_kraken_api_module_for_project(project, file) as (api_module, project_module):
            code = compile(file.read_text(), filename=file, mode="exec")
            exec(code, vars(project_module))


@contextlib.contextmanager
def inject_kraken_api_module_for_project(
    project: Project,
    file: Path,
) -> Iterator[tuple[types.ModuleType, types.ModuleType]]:
    api_module_name = "kraken.api"

    # Create the temporary replacement for the kraken.api module that the script will import from.
    api_module: Any = types.ModuleType(api_module_name)
    api_module.ctx = project.context
    api_module.project = project

    # In order for @dataclass decorators to work in a Python script loaded by this build, it must be
    # able to look up the module in sys.modules.
    project_module = types.ModuleType(f"_kraken__{project.name}_{id(project)}")
    project_module.__file__ = str(file)

    old_module = sys.modules.get(api_module_name)
    try:
        sys.modules[api_module_name] = api_module
        sys.modules[project_module.__name__] = project_module
        yield api_module, project_module
    finally:
        del sys.modules[project_module.__name__]
        if old_module is None:
            sys.modules.pop(api_module_name)
        else:
            sys.modules[api_module_name] = old_module
