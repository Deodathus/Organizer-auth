
from src.modules.shared.application.messanger import Command, CommandHandler
from src.modules.auth.application.dtos import CreateUser
from src.modules.auth.application.services import PasswordHasher
from src.modules.auth.domain.repositories import UserRepository
from src.modules.auth.domain.entities import User
from src.modules.auth.domain.value_objects import Email, Password


class RegisterUser(Command):
    def __init__(self, user: CreateUser):
        self._user = user

    def get_user(self) -> CreateUser:
        return self._user


class RegisterUserCommandHandler(CommandHandler):
    def __init__(self, user_repository: UserRepository, password_hasher: PasswordHasher):
        self._user_repository = user_repository
        self._password_hasher = password_hasher

    def handle(self, command: RegisterUser) -> None:
        password = self._password_hasher.hash(command.get_user().get_password())

        self._user_repository.store(
            User.register(
                command.get_user().get_login(),
                Email(command.get_user().get_email()),
                Password(password['hashed'], password['salt'])
            )
        )
