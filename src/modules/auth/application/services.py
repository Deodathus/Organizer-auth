import datetime

import bcrypt

from src.modules.auth.application.dtos import Token
from src.modules.auth.domain.value_objects import UserId, Password


class PasswordHasher(object):
    _encoding = 'UTF-8'

    def hash(self, raw_password: str) -> dict:
        password = bytes(raw_password, self._encoding)
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt)

        return {
            'hashed': hashed,
            'salt': salt
        }


class TokenCreator(object):
    def create(self, user_id: UserId, password: Password) -> Token:
        return Token('test', 3000, datetime.datetime(2023, 6, 16, 12, 3, 25))
