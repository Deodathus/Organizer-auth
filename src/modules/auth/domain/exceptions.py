
class UserWithGivenCredentialsDoesNotExist(Exception):
    @staticmethod
    def with_login(login: str) -> Exception:
        return UserWithGivenCredentialsDoesNotExist(f'User login: {login}')


class UserWithGivenLoginAlreadyExists(Exception):
    @staticmethod
    def with_login(login: str) -> Exception:
        return UserWithGivenLoginAlreadyExists(f'User login: {login}')


class UserWithGivenIdDoesNotExist(Exception):
    @staticmethod
    def with_id(user_id: str) -> Exception:
        return UserWithGivenIdDoesNotExist(f'User id: {user_id}')
