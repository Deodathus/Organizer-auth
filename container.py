
from dependency_injector import containers, providers
from src.modules.project.infrastructure.containers import ProjectContainer
from src.modules.auth.infrastructure.containers import AuthContainer


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=['config.ini'])

    wiring_config = containers.WiringConfiguration(modules=[
        'src.modules.auth.infrastructure.http.controllers',
        'src.modules.project.infrastructure.http.routes',
    ])

    project = providers.Container(
        ProjectContainer
    )

    auth = providers.Container(
        AuthContainer
    )
