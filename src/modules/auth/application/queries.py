import datetime

from src.modules.auth.application.dtos import UserToLogin, LoggedUser, UserDTO
from src.modules.auth.application.exceptions import InvalidCredentials, UserDoesNotExist
from src.modules.auth.application.services import PasswordHasher
from src.modules.auth.domain.entities import Token
from src.modules.auth.domain.exceptions import UserWithGivenCredentialsDoesNotExist, UserWithGivenIdDoesNotExist, \
    UserWithGivenTokenDoesNotExist
from src.modules.auth.domain.repositories import UserRepository
from src.modules.auth.domain.value_objects import UserCredentials, Password, Login, UserId, TokenValue
from src.modules.shared.application.messenger import Query, QueryHandler


class FetchTokenByCredentials(Query):
    def __init__(self, user: UserToLogin):
        self._user = user

    def get_user(self) -> UserToLogin:
        return self._user


class FetchTokenByCredentialsHandler(QueryHandler):
    def __init__(self, user_repository: UserRepository, password_hasher: PasswordHasher):
        self._user_repository = user_repository
        self._password_hasher = password_hasher

    def handle(self, query: FetchTokenByCredentials) -> LoggedUser:
        try:
            salt = self._user_repository.fetch_salt_by_login(
                Login(query.get_user().get_login())
            )

            token = self._user_repository.fetch_token_by_credentials(
                UserCredentials(
                    query.get_user().get_login(),
                    Password(
                        self._password_hasher.hash_with_salt(query.get_user().get_password(), salt)['hashed'],
                        salt
                    )
                )
            )
        except UserWithGivenCredentialsDoesNotExist:
            raise InvalidCredentials.create()

        return LoggedUser(token.get_token().get_token_value(), token.get_valid_time(), token.get_created_at())


class FetchUserById(Query):
    def __init__(self, user_id: str):
        self._user_id = user_id

    def get_user_id(self) -> str:
        return self._user_id


class FetchUserByIdHandler(QueryHandler):
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def handle(self, query: FetchUserById) -> UserDTO:
        try:
            user = self._user_repository.fetch_by_id(UserId.from_string(query.get_user_id()))

            return UserDTO(
                query.get_user_id(),
                user.get_token().get_token().get_token_value(),
                user.get_token().get_refresh_token().get_token_value(),
                user.get_token().get_valid_time(),
                user.get_token().get_created_at(),
                user.get_email().get_email()
            )
        except UserWithGivenIdDoesNotExist:
            raise UserDoesNotExist


class FetchUserByToken(Query):
    def __init__(self, token: str):
        self._api_token = token

    def get_api_token(self) -> str:
        return self._api_token


class FetchUserByTokenHandler(QueryHandler):
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def handle(self, query: FetchUserByToken) -> UserDTO:
        try:
            user = self._user_repository.fetch_by_token(TokenValue(query.get_api_token()))

            return UserDTO(
                user.get_user_id(),
                user.get_token().get_token().get_token_value(),
                user.get_token().get_refresh_token().get_token_value(),
                user.get_token().get_valid_time(),
                user.get_token().get_created_at(),
                user.get_email().get_email()
            )
        except UserWithGivenTokenDoesNotExist:
            raise UserDoesNotExist
