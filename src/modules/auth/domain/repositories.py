
from .entities import User


class UserRepository(object):
    """An interface to project repository"""

    ...

    def store(self, user: User) -> None:
        pass
