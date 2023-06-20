
class UserWithGivenCredentialsDoesNotExist(Exception):
    @staticmethod
    def with_login(login: str) -> Exception:
        return UserWithGivenCredentialsDoesNotExist(f'User login: {login}')

