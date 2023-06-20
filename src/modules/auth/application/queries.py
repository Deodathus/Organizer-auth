import datetime

from src.modules.auth.application.dtos import UserToLogin, LoggedUser, Token
from src.modules.auth.application.exceptions import InvalidCredentials
from src.modules.auth.domain.exceptions import UserWithGivenCredentialsDoesNotExist
from src.modules.auth.domain.repositories import UserRepository
from src.modules.auth.domain.value_objects import UserCredentials, Password, Login
from src.modules.shared.application.messenger import Query, QueryHandler


class FetchTokenByCredentials(Query):
    def __init__(self, user: UserToLogin):
        self._user = user

    def get_user(self) -> UserToLogin:
        return self._user


class FetchTokenByCredentialsHandler(QueryHandler):
    def __init__(self, user_repository: UserRepository, password_hasher):
        self._user_repository = user_repository

    def handle(self, query: FetchTokenByCredentials) -> LoggedUser:
        try:
            salt = self._user_repository.fetch_salt_by_login(
                Login(query.get_user().get_login())
            )
        except UserWithGivenCredentialsDoesNotExist:
            raise InvalidCredentials.create()


        # token = self._user_repository.fetch_token_by_credentials(
        #     UserCredentials(
        #         query.get_user().get_login(),
        #         Password(
        #
        #         )
        #     )
        # )

        return LoggedUser(
            Token('', 1, datetime.datetime(2023, 10, 5))
        )
