
from src.modules.shared.application.messenger import Command, CommandHandler
from src.modules.project.domain.repositories import ProjectRepository
from src.modules.project.domain.entities import Project
from src.modules.project.domain.value_objects import ProjectId


class StoreProject(Command):
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name


class StoreProjectCommandHandler(CommandHandler):
    def __init__(self, project_repository: ProjectRepository):
        self._project_repository = project_repository

    def handle(self, command: StoreProject):
        self._project_repository.store(
            Project(
                ProjectId.generate(),
                command.get_name()
            )
        )


class DeleteProject(Command):
    def __init__(self, project_id: str):
        self._project_id = project_id

    def get_project_id(self) -> ProjectId:
        return ProjectId.from_string(self._project_id)


class DeleteProjectCommandHandler(CommandHandler):
    def __init__(self, project_repository: ProjectRepository):
        self._project_repository = project_repository

    def handle(self, command: DeleteProject):
        self._project_repository.delete(command.get_project_id())


class UpdateProject(Command):
    def __init__(self, project_id: str, project_name: str):
        self._project_id = project_id
        self._project_name = project_name

    def get_project_id(self) -> ProjectId:
        return ProjectId.from_string(self._project_id)

    def get_project_name(self) -> str:
        return self._project_name


class UpdateProjectCommandHandler(CommandHandler):
    def __init__(self, project_repository: ProjectRepository):
        self._project_repository = project_repository

    def handle(self, command: UpdateProject) -> None:
        self._project_repository.update(command.get_project_id(), command.get_project_name())
