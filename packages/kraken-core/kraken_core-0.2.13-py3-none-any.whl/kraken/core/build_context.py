from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Iterator, Optional, TypeVar

from .pyenv import PyenvManager

if TYPE_CHECKING:
    from .project import Project
    from .task import Task

T = TypeVar("T")


class BuildContext:
    """This class is the single instance where all components of a build process come together."""

    def __init__(self, build_directory: Path) -> None:
        self._root_project: Optional[Project] = None
        self.build_directory = build_directory
        self.pyenv = PyenvManager(build_directory / ".lib")
        self.metadata: list[Any] = []

    def find_metadata(self, of_type: type[T]) -> T | None:
        """Returns the first entry in the :attr:`metadata` that is of the specified type."""

        return next((x for x in self.metadata if isinstance(x, of_type)), None)

    @property
    def root_project(self) -> Project:
        assert self._root_project is not None, "BuildContext.root_project is not set"
        return self._root_project

    @root_project.setter
    def root_project(self, project: Project) -> None:
        assert self._root_project is None, "BuildContext.root_project is already set"
        self._root_project = project

    def load_project(
        self,
        file: Path | None = None,
        directory: Path | None = None,
        parent: Project | None = None,
    ) -> Project:
        """Loads a project from a file or directory.

        Args:
            file: The file to load from. One of *file* or *directory* must be specified.
            directory: The directory to load from. If it is not specified, and the matching loader
                does not return a directory, the parent directory of *file* is used. If a directory
                is specified and the loader returns a different directory, the directory passed her
                takes precedence.
            parent: The parent project. If no parent is specified, then the :attr:`root_project`
                must not have been initialized yet and the loaded project will be initialize it.
                If the root project is initialized but no parent is specified, an error will be
                raised.
        """

        from .loader import detect_project_loader
        from .project import Project

        file, directory, loader = detect_project_loader(file, directory)

        project = Project(directory.name, directory, parent, self)

        if self._root_project is None:
            self._root_project = project

        loader.load_script(file, project)

        return project

    def iter_projects(self) -> Iterator[Project]:
        """Iterates over all projects in the context."""

        def _recurse(project: Project) -> Iterator[Project]:
            yield project
            for child_project in project.children().values():
                yield from _recurse(child_project)

        yield from _recurse(self.root_project)

    def resolve_tasks(self, targets: list[str] | None, relative_to: Project | None = None) -> list[Task]:
        """Resolve the given project or task references in *targets* relative to the specified project, or by
        default relative to the root project. A target is a colon-separated string that behaves similar to a
        filesystem path to address projects and tasks in the hierarchy. The root project is represented with a
        single colon and cannot be referenced by its name.

        A target that is just a task name will match all tasks of that name."""

        relative_to = relative_to or self.root_project

        if targets is None:
            # Return all default tasks.
            return [task for project in self.iter_projects() for task in project.tasks().values() if task.default]

        tasks: list[Task] = []
        count = 0
        target: str

        def _check_matched() -> None:
            nonlocal count
            if count == len(tasks):
                raise ValueError(f"no tasks matched selector {target!r}")
            count = len(tasks)

        for target in targets:
            count = len(tasks)

            if ":" not in target:
                # Select all targets with a name matching the specified target.
                tasks.extend(
                    task for project in self.iter_projects() for task in project.tasks().values() if task.name == target
                )
                _check_matched()
                continue

            # Resolve as many components in the project hierarchy as possible.
            project = relative_to
            parts = target.split(":")
            if parts[0] == "":
                project = self.root_project
                parts.pop(0)
            while parts:
                project_children = project.children()
                if parts[0] in project_children.values():
                    project = project_children[parts.pop(0)]
                else:
                    break

            project_tasks = project.tasks()
            if not parts or parts == [""]:
                # The project was selected, add all default tasks.
                tasks.extend(task for task in project_tasks.values() if task.default)
            elif len(parts) == 1:
                # A specific target is selected.
                if parts[0] not in project_tasks:
                    raise ValueError(f"task {target!r} does not exist")
                tasks.append(project_tasks[parts[0]])
            else:
                # Some project in the path does not exist.
                raise ValueError(f"project {':'.join(target.split(':')[:-1])} does not exist")

            _check_matched()

        return tasks

    def finalize(self) -> None:
        """Call :meth:`Task.finalize()` on all tasks. This should be called before a graph is created."""

        for project in self.iter_projects():
            for task in project.tasks().values():
                task.finalize()

    @staticmethod
    def current() -> BuildContext | None:
        """Returns the current build context if it exists."""

        try:
            from kraken.api import ctx

            return ctx
        except RuntimeError:
            return None
