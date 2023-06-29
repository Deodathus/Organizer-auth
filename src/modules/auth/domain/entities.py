
from __future__ import annotations

import datetime

from src.modules.auth.domain.value_objects import UserId, Email, Password, UserStatus, Login, TokenValue, TokenId


class Token(object):
    """14 days / 336 hours"""
    _TOKEN_VALID_TIME = 1209600

    _token_id: TokenId
    _user_id: UserId
    _token: TokenValue
    _valid_time: int
    _active: bool
    _created_at: datetime.datetime

    def __init__(
            self,
            token_id: TokenId,
            user_id: UserId,
            token: TokenValue,
            valid_time: int,
            active: bool,
            created_at: datetime.datetime = datetime.datetime
    ):
        self._token_id = token_id
        self._user_id = user_id
        self._token = token
        self._valid_time = valid_time
        self._active = active
        self._created_at = created_at

    @staticmethod
    def create(user_id: UserId, token: TokenValue) -> Token:
        return Token(
            TokenId.generate(),
            user_id,
            token,
            Token._TOKEN_VALID_TIME,
            True
        )

    @staticmethod
    def reproduce(
            token_id: TokenId,
            user_id: UserId,
            token: TokenValue,
            valid_time: int,
            active: bool,
            created_at: datetime.datetime
    ) -> Token:
        return Token(
            token_id,
            user_id,
            token,
            valid_time,
            active,
            created_at
        )

    def get_id(self) -> TokenId:
        return self._token_id

    def get_user_id(self) -> UserId:
        return self._user_id

    def get_token(self) -> TokenValue:
        return self._token

    def get_valid_time(self) -> int:
        return self._valid_time

    def get_active(self) -> bool:
        return self._active

    def get_created_at(self) -> datetime.datetime:
        return self._created_at


class User(object):
    _user_id: UserId
    _login: Login
    _email: Email
    _password: Password
    _status: UserStatus
    _token: Token

    def __init__(
        self, user_id: UserId, login: Login, email: Email, password: Password, status: UserStatus, token: Token
    ):
        self._user_id = user_id
        self._login = login
        self._email = email
        self._password = password
        self._status = status
        self._token = token

    @staticmethod
    def reproduce(
        user_id: UserId, login: Login, email: Email, password: Password, status: UserStatus, token: Token
    ) -> User:
        user = User(
            user_id,
            login,
            email,
            password,
            status,
            token
        )

        return user

    @staticmethod
    def register(user_id: UserId, login: Login, email: Email, password: Password, token: Token) -> User:
        return User(
            user_id,
            login,
            email,
            password,
            UserStatus.ACTIVE,
            token
        )

    def get_user_id(self) -> UserId:
        return self._user_id

    def get_login(self) -> Login:
        return self._login

    def get_email(self) -> Email:
        return self._email

    def get_password(self) -> Password:
        return self._password

    def get_status(self) -> UserStatus:
        return self._status

    def get_token(self) -> Token:
        return self._token
