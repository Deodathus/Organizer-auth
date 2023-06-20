
class InvalidCredentials(Exception):
    @staticmethod
    def create() -> Exception:
        return InvalidCredentials()
