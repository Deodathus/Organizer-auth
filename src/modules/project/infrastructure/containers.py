
from dependency_injector import containers, providers
from src.modules.project.infrastructure.repositories import MysqlProjectRepository
from src.modules.project.application.queries import GetAllProjectsQueryHandler, GetAllProjects
from src.modules.project.application.commands import StoreProjectCommandHandler, StoreProject, \
    DeleteProjectCommandHandler, DeleteProject, UpdateProjectCommandHandler, UpdateProject
from src.modules.shared.infrastructure.messenger import QueryBus, CommandBus


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

    # command handlers
    store_project_command_handler = providers.Factory(
        StoreProjectCommandHandler,
        project_repository
    )

    delete_project_command_handler = providers.Factory(
        DeleteProjectCommandHandler,
        project_repository
    )

    update_project_command_handler = providers.Factory(
        UpdateProjectCommandHandler,
        project_repository
    )

    # messenger
    command_bus = providers.Factory(
        CommandBus,
        providers.Dict({
            StoreProject: store_project_command_handler,
            DeleteProject: delete_project_command_handler,
            UpdateProject: update_project_command_handler
        })
    )

    query_bus = providers.Factory(
        QueryBus,
        providers.Dict({
            GetAllProjects: get_all_projects_query_handler
        })
    )

