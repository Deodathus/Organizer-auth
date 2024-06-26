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


class UserDTO(object):
    def __init__(
        self,
        user_id: str,
        token: str,
        refresh_token: str,
        token_valid_time: int,
        token_created_at: datetime.datetime,
        email: str
    ):
        self._user_id = user_id
        self._token = token
        self._refresh_token = refresh_token
        self._token_valid_time = token_valid_time
        self._token_created_at = token_created_at
        self._email = email

    def get_user_id(self) -> str:
        return self._user_id

    def get_token(self) -> str:
        return self._token

    def get_refresh_token(self) -> str:
        return self._refresh_token

    def get_token_valid_time(self) -> str:
        return self._token_valid_time

    def get_token_created_at(self) -> datetime.datetime:
        return self._token_created_at
