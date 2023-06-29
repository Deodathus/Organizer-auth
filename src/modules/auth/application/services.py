import datetime
import uuid

import bcrypt

from src.modules.auth.application.dtos import CreatedToken
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

    def hash_with_salt(self, raw_password: str, salt: str):
        password = bytes(raw_password, self._encoding)
        hashed = bcrypt.hashpw(password, bytes(salt, self._encoding))

        return {
            'hashed': hashed,
        }


class TokenCreator(object):
    def create(self, user_id: UserId, password: Password) -> CreatedToken:
        return CreatedToken(str(uuid.uuid4()))
