
from src.modules.auth.domain.repositories import UserRepository
from src.modules.auth.domain.entities import User
from sqlalchemy import create_engine, text

engine = create_engine('mysql://organizer-auth:password@organizer-auth-db/organizer_auth')
connection = engine.connect()


class MysqlUserRepository(UserRepository):
    """User repository implementation"""
    _TABLE_NAME = 'users'

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
