from src.modules.auth.module_api.events import UserRegistered
from src.modules.project.application.services import UserWebhookRequestTriggererInterface
from src.modules.project.domain.repositories import ProjectWebhookRepository
from src.modules.project.domain.value_objects import ProjectId, ProjectWebhookType
from src.modules.shared.application.messenger import EventHandler, Event


class TriggerRegisteredWebhook(EventHandler):
    def __init__(
        self,
        webhook_triggerer: UserWebhookRequestTriggererInterface,
        project_webhook_repository: ProjectWebhookRepository
    ):
        self._webhook_triggerer = webhook_triggerer
        self._project_webhook_repository = project_webhook_repository

    def handle(self, event: UserRegistered) -> None:
        webhook = self._project_webhook_repository.get_by_project_id_and_type(
            ProjectId.from_string(event.get_project_id()),
            ProjectWebhookType.REGISTER
        )

        self._webhook_triggerer.trigger(webhook.get_url().get_value(), event.get_user_id())
