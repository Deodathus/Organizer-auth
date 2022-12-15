
from dependency_injector import containers, providers
from src.modules.auth.application.services import PasswordHasher
from src.modules.auth.application.commands import RegisterUser, RegisterUserCommandHandler
from src.modules.auth.infrastructure.repositories import MysqlUserRepository
from src.modules.shared.infrastructure.messanger import QueryBus, CommandBus


class AuthContainer(containers.DeclarativeContainer):
    # services
    password_hasher = providers.Factory(
        PasswordHasher
    )

    # repositories
    user_repository = providers.Factory(
        MysqlUserRepository
    )

    # query handlers

    # command handlers
    register_user_command_handler = providers.Factory(
        RegisterUserCommandHandler,
        user_repository,
        password_hasher
    )

    # messenger
    command_bus = providers.Factory(
        CommandBus,
        providers.Dict({
            RegisterUser: register_user_command_handler
        })
    )
