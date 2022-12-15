
from enum import Enum
from src.modules.shared.domain.value_objects import ID


class UserId(ID):
    pass


class Email(object):
    _email: str

    def __init__(self, email: str):
        self._email = email

    def get_email(self) -> str:
        return self._email


class Password(object):
    _password: str
    _salt: str

    def __init__(self, password: str, salt: str):
        self._password = password
        self._salt = salt

    def get_password(self) -> str:
        return self._password

    def get_salt(self) -> str:
        return self._salt


class UserStatus(Enum):
    DISABLED = 0
    ACTIVE = 1
    BANNED = 2

