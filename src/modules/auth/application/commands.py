
from src.modules.auth.application.exceptions import LoginAlreadyTaken
from src.modules.auth.domain.exceptions import UserWithGivenLoginAlreadyExists
from src.modules.auth.module_api.events import UserRegistered
from src.modules.shared.application.messenger import Command, CommandHandler, EventBus
from src.modules.auth.application.dtos import CreateUser, UserToLogin, LoggedUser
from src.modules.auth.application.services import PasswordHasher, TokenCreator
from src.modules.auth.domain.repositories import UserRepository
from src.modules.auth.domain.entities import User, Token
from src.modules.auth.domain.value_objects import Email, Password, Login, UserId, TokenValue as TokenValue, \
    RefreshTokenValue


class RegisterUser(Command):
    def __init__(self, user: CreateUser):
        self._user = user

    def get_user(self) -> CreateUser:
        return self._user


class RegisterUserCommandHandler(CommandHandler):
    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher,
        token_creator: TokenCreator,
        event_bus: EventBus
    ):
        self._user_repository = user_repository
        self._password_hasher = password_hasher
        self._token_creator = token_creator
        self._event_bus = event_bus

    def handle(self, command: RegisterUser) -> None:
        password = self._password_hasher.hash(command.get_user().get_password())
        user_id = UserId.generate()
        hashed_password = Password(password['hashed'], password['salt'])

        try:
            self._user_repository.store(
                User.register(
                    user_id,
                    Login(command.get_user().get_login()),
                    Email(command.get_user().get_email()),
                    hashed_password,
                    Token.create(
                        user_id,
                        TokenValue(self._token_creator.create().get_value()),
                        RefreshTokenValue(self._token_creator.create().get_value())
                    )
                )
            )

            self._event_bus.dispatch(
                UserRegistered(
                    user_id.value,
                    '90b9e3d6-8b6b-4552-a101-3fbdca5e7615'
                )
            )
        except UserWithGivenLoginAlreadyExists:
            raise LoginAlreadyTaken.create()


class LoginUser(Command):
    def __init__(self, user: UserToLogin):
        self._user = user

    def get_user(self) -> UserToLogin:
        return self._user


class LoginUserCommandHandler(CommandHandler):
    def __init__(self, user_repository: UserRepository, password_hasher: PasswordHasher):
        self._user_repository = user_repository
        self._password_hasher = password_hasher

