from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from src.modules.auth.module_api.events import UserRegistered
from src.modules.project.application.event_handlers import TriggerRegisteredWebhook
from src.modules.project.infrastructure.adapters import UserWebhookRequestTriggerer
from src.modules.project.infrastructure.repositories import MysqlProjectWebhookRepository
from src.modules.shared.infrastructure.messenger import EventBus


class EventBusContainer(DeclarativeContainer):
    # services
    user_webhook_triggerer = providers.Factory(
        UserWebhookRequestTriggerer
    )

    # repositories
    project_webhook_repository = providers.Factory(
        MysqlProjectWebhookRepository
    )

    # event handlers
    # --- project
    trigger_registered_webhook = providers.Factory(
        TriggerRegisteredWebhook,
        user_webhook_triggerer,
        project_webhook_repository
    )

    # event bus
    event_bus = providers.Factory(
        EventBus,
        providers.Dict({
            UserRegistered: trigger_registered_webhook
        })
    )
