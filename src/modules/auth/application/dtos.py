

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
