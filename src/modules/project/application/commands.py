
from src.modules.shared.application.messanger import Command, CommandHandler
from src.modules.project.domain.repositories import ProjectRepository
from src.modules.project.domain.entities import Project
from src.modules.project.domain.value_objects import ProjectId


class StoreProject(Command):
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name


class StoreProjectCommandHandler(CommandHandler):
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def handle(self, command: StoreProject):
        self.project_repository.store(
            Project(
                ProjectId.generate(),
                command.get_name()
            )
        )

