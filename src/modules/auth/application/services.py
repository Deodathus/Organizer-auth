
import bcrypt


class PasswordHasher(object):
    _encoding = 'UTF-8'

    def hash(self, raw_password) -> dict:
        password = bytes(raw_password, self._encoding)
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt)

        return {
            'hashed': hashed,
            'salt': salt
        }
