
from dependency_injector import containers, providers
from src.modules.project.infrastructure.repositories import MysqlProjectRepository, MysqlProjectWebhookRepository
from src.modules.project.application.queries import GetAllProjectsQueryHandler, GetAllProjects
from src.modules.project.application.commands import StoreProjectCommandHandler, StoreProject, \
    DeleteProjectCommandHandler, DeleteProject, UpdateProjectCommandHandler, UpdateProject, StoreProjectWebhookHandler, \
    StoreProjectWebhook
from src.modules.shared.infrastructure.messenger import QueryBus, CommandBus


class ProjectContainer(containers.DeclarativeContainer):
    event_bus = None

    # repositories
    project_repository = providers.Factory(
        MysqlProjectRepository
    )
    project_webhook_repository = providers.Factory(
        MysqlProjectWebhookRepository
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

    store_project_webhook_command_handler = providers.Factory(
        StoreProjectWebhookHandler,
        project_webhook_repository,
        project_repository
    )

    # messenger
    command_bus = providers.Factory(
        CommandBus,
        providers.Dict({
            StoreProject: store_project_command_handler,
            DeleteProject: delete_project_command_handler,
            UpdateProject: update_project_command_handler,
            StoreProjectWebhook: store_project_webhook_command_handler
        })
    )

    query_bus = providers.Factory(
        QueryBus,
        providers.Dict({
            GetAllProjects: get_all_projects_query_handler
        })
    )

