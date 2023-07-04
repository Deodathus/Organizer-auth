
from dependency_injector import containers, providers

from src.modules.auth.module_api.events import UserRegistered
from src.modules.project.infrastructure.adapters import UserWebhookRequestTriggerer
from src.modules.project.infrastructure.containers import ProjectContainer
from src.modules.auth.infrastructure.containers import AuthContainer
from src.modules.project.infrastructure.repositories import MysqlProjectWebhookRepository
from src.modules.shared.infrastructure.messenger import EventBus


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=['config.ini'])

    wiring_config = containers.WiringConfiguration(modules=[
        'src.modules.auth.infrastructure.http.controllers',
        'src.modules.project.infrastructure.http.controllers',
    ])

    # services
    registered_webhook_triggerer = providers.Factory(
        UserWebhookRequestTriggerer
    )

    # repositories
    project_webhook_repository = providers.Factory(
        MysqlProjectWebhookRepository
    )

    # event handlers
    # --- project
    trigger_registered_webhook = providers.Factory(
        registered_webhook_triggerer,
        project_webhook_repository
    )

    # event bus
    event_bus = providers.Factory(
        EventBus,
        providers.Dict({
            UserRegistered: trigger_registered_webhook
        })
    )

    project = providers.Container(
        ProjectContainer
    )

    auth = providers.Container(
        AuthContainer,
        {
            'event_bus': event_bus
        }
    )
