
from dependency_injector import containers, providers
from src.modules.project.infrastructure.containers import ProjectContainer


class ApplicationContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[
        'src.modules.project.infrastructure.http.routes'
    ])

    project = providers.Container(
        ProjectContainer
    )
