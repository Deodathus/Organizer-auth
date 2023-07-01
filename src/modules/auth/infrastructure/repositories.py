from sqlalchemy.exc import NoResultFound, IntegrityError

from src.modules.auth.domain.exceptions import UserWithGivenCredentialsDoesNotExist, UserWithGivenLoginAlreadyExists, \
    UserWithGivenIdDoesNotExist
from src.modules.auth.domain.repositories import UserRepository
from src.modules.auth.domain.entities import User, Token
from sqlalchemy import create_engine, text

from src.modules.auth.domain.value_objects import UserCredentials, Login, TokenId, TokenValue, UserId, UserStatus, \
    Email, DummyPassword, RefreshTokenValue

engine = create_engine('mysql://organizer-auth:password@organizer-auth-db/organizer_auth')
connection = engine.connect()


class MysqlUserRepository(UserRepository):
    """User repository implementation"""
    _TABLE_NAME = 'users'
    _TOKEN_TABLE_NAME = 'user_tokens'

    def store(self, user: User) -> None:
        try:
            connection.begin()
            connection.execute(
                text(
                    f'insert into {self._TABLE_NAME} '
                    f'(id, login, email, password, salt, status, created_at) '
                    f'values (:id, :login, :email, :password, :salt, :status, NOW())'
                ),
                {
                    'id': str(user.get_user_id().value),
                    'login': user.get_login().get_login(),
                    'email': user.get_email().get_email(),
                    'password': user.get_password().get_password(),
                    'salt': user.get_password().get_salt(),
                    'status': user.get_status().value
                }
            )

            connection.execute(
                text(
                    f'insert into {self._TOKEN_TABLE_NAME} '
                    f'(id, user_id, token, refresh_token, valid_time, active, created_at) '
                    f'values (:id, :user_id, :token, :refresh_token, :valid_time, :active, NOW())'
                ),
                {
                    'id': str(user.get_token().get_id().value),
                    'user_id': user.get_user_id().value,
                    'token': user.get_token().get_token().get_token_value(),
                    'refresh_token': user.get_token().get_refresh_token().get_token_value(),
                    'valid_time': user.get_token().get_valid_time(),
                    'active': user.get_token().get_active()
                }
            )

            connection.connection.commit()
        except IntegrityError:
            raise UserWithGivenLoginAlreadyExists.with_login(user.get_login().get_login())

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
        try:
            user_id = connection.execute(
                text(
                    f'select id from {self._TABLE_NAME} where login = :login and password = :password'
                ),
                {
                    'login': credentials.get_login(),
                    'password': credentials.get_password().get_password(),
                }
            ).one()

            raw_result = connection.execute(
                text(
                    f'select id, user_id, token, refresh_token, valid_time, active, created_at from {self._TOKEN_TABLE_NAME} '
                    f'where user_id = :user_id'
                ),
                {
                    'user_id': user_id[0],
                    'active': True
                }
            ).one()

            return Token.reproduce(
                TokenId.from_string(raw_result.id),
                UserId.from_string(raw_result.user_id),
                TokenValue(raw_result.token),
                RefreshTokenValue(raw_result.refresh_token),
                raw_result.valid_time,
                raw_result.active,
                raw_result.created_at
            )
        except NoResultFound:
            raise UserWithGivenCredentialsDoesNotExist.with_login(credentials.get_login())

    def fetch_by_id(self, user_id: UserId) -> User:
        try:
            user_data = connection.execute(
                text(
                    f'select login, email, status from {self._TABLE_NAME} where id = :id and status = :status'
                ),
                {
                    'id': user_id.value,
                    'status': UserStatus.ACTIVE.value
                }
            ).fetchone()

            if user_data is None:
                raise UserWithGivenIdDoesNotExist

            user_token = connection.execute(
                text(
                    f'select id, token, refresh_token, valid_time, active, created_at '
                    f'from {self._TOKEN_TABLE_NAME} where user_id = :user_id'
                ),
                {
                    'user_id': user_id.value
                }
            ).fetchone()

            return User.reproduce(
                user_id,
                Login(user_data.login),
                Email(user_data.email),
                DummyPassword(),
                UserStatus[user_data.status.upper()],
                Token.reproduce(
                    TokenId.from_string(user_token.id),
                    user_id,
                    TokenValue(user_token.token),
                    RefreshTokenValue(user_token.refresh_token),
                    user_token.valid_time,
                    user_token.active,
                    user_token.created_at
                )
            )
        except NoResultFound:
            raise UserWithGivenIdDoesNotExist
