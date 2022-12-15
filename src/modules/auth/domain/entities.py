
from __future__ import annotations
from src.modules.auth.domain.value_objects import UserId, Email, Password, UserStatus


class User(object):
    _user_id: UserId
    _login: str
    _email: Email
    _password: Password
    _status: UserStatus

    def __init__(self, user_id: UserId, login: str, email: Email, password: Password, status: UserStatus):
        self._user_id = user_id
        self._login = login
        self._email = email
        self._password = password
        self._status = status

    @staticmethod
    def register(login: str, email: Email, password: Password) -> User:
        return User(
            UserId.generate(),
            login,
            email,
            password,
            UserStatus.ACTIVE
        )

    def get_user_id(self) -> UserId:
        return self._user_id

    def get_login(self) -> str:
        return self._login

    def get_email(self) -> Email:
        return self._email

    def get_password(self) -> Password:
        return self._password

    def get_status(self) -> UserStatus:
        return self._status
