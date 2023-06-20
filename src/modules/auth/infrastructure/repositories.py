from sqlalchemy.exc import NoResultFound

from src.modules.auth.domain.exceptions import UserWithGivenCredentialsDoesNotExist
from src.modules.auth.domain.repositories import UserRepository
from src.modules.auth.domain.entities import User
from sqlalchemy import create_engine, text

from src.modules.auth.domain.value_objects import Token, UserCredentials, Login

engine = create_engine('mysql://organizer-auth:password@organizer-auth-db/organizer_auth')
connection = engine.connect()


class MysqlUserRepository(UserRepository):
    """User repository implementation"""
    _TABLE_NAME = 'users'
    _TOKEN_TABLE_NAME = 'user_tokens'

    def store(self, user: User) -> None:
        connection.execute(
            text(
                f'insert into {self._TABLE_NAME} '
                f'(id, login, email, password, salt, status, created_at) '
                f'values (:id, :login, :email, :password, :salt, :status, NOW())'
            ),
            {
                'id': str(user.get_user_id().value),
                'login': user.get_login(),
                'email': user.get_email().get_email(),
                'password': user.get_password().get_password(),
                'salt': user.get_password().get_salt(),
                'status': user.get_status().value
            }
        )

    def fetch_salt_by_login(self, login: Login) -> str:
        try:
            raw_data = connection.execute(
                text(
                    f'select salt from {self._TABLE_NAME} where login = :login'
                ),
                {
                    'login': str(login.get_login())
                }
            ).one()

            return raw_data.salt
        except NoResultFound:
            raise UserWithGivenCredentialsDoesNotExist.with_login(login.get_login())

    def fetch_token_by_credentials(self, credentials: UserCredentials) -> Token:
        user_id = connection.execute(
            text(
                f'select id from {self._TABLE_NAME} where login = :login and password = :password',
                {
                    'login': credentials.get_login(),
                    'password': credentials.get_password(),
                }
            )
        )

        print(user_id)

        raw_result = connection.execute(
            text(
                f'select token, valid_time from {self._TOKEN_TABLE_NAME} where user_id = :user_id',
                {
                    'user_id': user_id
                }
            )
        )

        return Token('1', 100)
