
from .entities import User, Token
from .value_objects import UserCredentials, Login, UserId


class UserRepository(object):
    """An interface to project repository"""

    ...

    def store(self, user: User) -> None:
        pass

    def fetch_salt_by_login(self, login: Login) -> str:
        pass

    def fetch_token_by_credentials(self, credentials: UserCredentials) -> Token:
        pass

    def fetch_by_id(self, user_id: UserId) -> User:
        pass

