import datetime


class CreateUser(object):
    def __init__(self, login: str, email: str, password: str):
        self._login = login
        self._email = email
        self._password = password

    def get_login(self) -> str:
        return self._login

    def get_email(self) -> str:
        return self._email

    def get_password(self) -> str:
        return self._password


class UserToLogin(object):
    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password

    def get_login(self) -> str:
        return self._login

    def get_password(self) -> str:
        return self._password


class CreatedToken(object):
    def __init__(self, token: str):
        self._token = token

    def get_value(self) -> str:
        return self._token


class LoggedUser(object):
    def __init__(self, token: str, valid_time: int, created_at: datetime.datetime):
        self._token = token
        self._valid_time = valid_time
        self._created_at = created_at

    def get_token(self) -> str:
        return self._token

    def get_valid_time(self) -> int:
        return self._valid_time

    def get_created_at(self) -> datetime.datetime:
        return self._created_at
