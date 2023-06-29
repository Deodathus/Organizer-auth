
class InvalidCredentials(Exception):
    @staticmethod
    def create() -> Exception:
        return InvalidCredentials()


class LoginAlreadyTaken(Exception):
    @staticmethod
    def create() -> Exception:
        return LoginAlreadyTaken()
