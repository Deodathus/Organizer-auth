
from src.modules.project.application.dtos import ProjectWebhookToStore
from src.modules.project.application.exceptions import InvalidWebhookType, ProjectDoesNotExist
from src.modules.shared.application.messenger import Command, CommandHandler
from src.modules.project.domain.repositories import ProjectRepository, ProjectWebhookRepository
from src.modules.project.domain.entities import Project, ProjectWebhook
from src.modules.project.domain.value_objects import ProjectId, ProjectWebhookType, ProjectWebhookUrl


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


class StoreProjectWebhook(Command):
    _webhook_to_store: ProjectWebhookToStore

    def __init__(self, webhook: ProjectWebhookToStore):
        self._webhook_to_store = webhook

    def get_webhook(self) -> ProjectWebhookToStore:
        return self._webhook_to_store


class StoreProjectWebhookHandler(CommandHandler):
    def __init__(self, project_webhook_repository: ProjectWebhookRepository, project_repository: ProjectRepository):
        self._project_webhook_repository = project_webhook_repository
        self._project_repository = project_repository

    def handle(self, command: StoreProjectWebhook) -> None:
        project_exists = self._project_repository.exists_by_id(
            ProjectId.from_string(command.get_webhook().get_project_id())
        )

        if not project_exists:
            raise ProjectDoesNotExist(command.get_webhook().get_project_id())

        if command.get_webhook().get_type() in ProjectWebhookType.__members__:
            webhook_type = ProjectWebhookType[command.get_webhook().get_type()]

            self._project_webhook_repository.store(
                ProjectWebhook.create(
                    ProjectId.from_string(command.get_webhook().get_project_id()),
                    webhook_type,
                    ProjectWebhookUrl(command.get_webhook().get_url())
                )
            )
        else:
            raise InvalidWebhookType.with_value(command.get_webhook().get_type())
