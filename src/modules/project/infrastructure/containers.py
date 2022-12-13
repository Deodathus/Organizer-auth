
from dependency_injector import containers, providers
from src.modules.project.infrastructure.repositories import MysqlProjectRepository
from src.modules.project.application.queries import GetAllProjectsQueryHandler, GetAllProjects
from src.modules.shared.infrastructure.messanger import QueryBus, CommandBus


class ProjectContainer(containers.DeclarativeContainer):

    # repositories
    project_repository = providers.Factory(
        MysqlProjectRepository
    )

    # query handlers
    get_all_projects_query_handler = providers.Factory(
        GetAllProjectsQueryHandler,
        project_repository
    )

    # messenger
    command_bus = providers.Factory(
        CommandBus
    )

    query_bus = providers.Factory(
        QueryBus,
        providers.Dict({
            GetAllProjects: get_all_projects_query_handler
        })
    )

