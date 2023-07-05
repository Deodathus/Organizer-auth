
from dependency_injector import containers, providers

from src.modules.project.infrastructure.containers import ProjectContainer
from src.modules.auth.infrastructure.containers import AuthContainer
from src.modules.shared.infrastructure.containers import EventBusContainer


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=['config.ini'])

    wiring_config = containers.WiringConfiguration(modules=[
        'src.modules.auth.infrastructure.http.controllers',
        'src.modules.project.infrastructure.http.controllers',
    ])

    event_bus = providers.Container(
        EventBusContainer
    )

    project = providers.Container(
        ProjectContainer
    )

    auth = providers.Container(
        AuthContainer,
        event_bus=event_bus
    )
