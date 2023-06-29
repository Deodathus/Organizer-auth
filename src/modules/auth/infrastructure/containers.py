
from dependency_injector import containers, providers

from src.modules.auth.application.queries import FetchTokenByCredentialsHandler, FetchTokenByCredentials
from src.modules.auth.application.services import PasswordHasher, TokenCreator
from src.modules.auth.application.commands import RegisterUser, RegisterUserCommandHandler
from src.modules.auth.infrastructure.repositories import MysqlUserRepository
from src.modules.shared.infrastructure.messenger import QueryBus, CommandBus


class AuthContainer(containers.DeclarativeContainer):
    # services
    password_hasher = providers.Factory(
        PasswordHasher
    )

    token_creator = providers.Factory(
        TokenCreator
    )

    # repositories
    user_repository = providers.Factory(
        MysqlUserRepository
    )

    # query handlers
    fetch_token_by_credentials_query_handler = providers.Factory(
        FetchTokenByCredentialsHandler,
        user_repository,
        password_hasher
    )

    # command handlers
    register_user_command_handler = providers.Factory(
        RegisterUserCommandHandler,
        user_repository,
        password_hasher,
        token_creator
    )

    # messenger
    command_bus = providers.Factory(
        CommandBus,
        providers.Dict({
            RegisterUser: register_user_command_handler
        })
    )

    query_bus = providers.Factory(
        QueryBus,
        providers.Dict({
            FetchTokenByCredentials: fetch_token_by_credentials_query_handler
        })
    )
