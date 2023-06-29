
from fastapi import APIRouter, status, Depends
from dependency_injector.wiring import inject, Provide
from fastapi import Response

from container import ApplicationContainer
from .models import AuthModel, RegisterModel
from src.modules.shared.application.messenger import CommandBus, QueryBus
from src.modules.auth.application.commands import RegisterUser
from src.modules.auth.application.dtos import CreateUser, UserToLogin
from ...application.exceptions import InvalidCredentials, LoginAlreadyTaken
from ...application.queries import FetchTokenByCredentials

router = APIRouter()


@router.get('/')
@inject
def index(version: str = Provide[ApplicationContainer.config.api.version]):
    return {
        "message": f'Version: {version}',
        "code": status.HTTP_200_OK
    }


@router.post('/user/login')
@inject
def login(
        auth_data: AuthModel,
        response: Response,
        query_bus: QueryBus = Depends(Provide[ApplicationContainer.auth.query_bus]),
) -> dict:
    try:
        token = query_bus.handle(
            FetchTokenByCredentials(
                UserToLogin(
                    auth_data.login,
                    auth_data.password
                )
            )
        )

        return {
            "message": token,
            "code": status.HTTP_200_OK
        }
    except InvalidCredentials:
        response.status_code = status.HTTP_403_FORBIDDEN

        return {
            "message": "Forbidden",
            "code": status.HTTP_403_FORBIDDEN
        }


@router.post('/user', status_code=status.HTTP_201_CREATED)
@inject
def register(
        register_data: RegisterModel,
        response: Response,
        command_bus: CommandBus = Depends(Provide[ApplicationContainer.auth.command_bus])
) -> dict:
    try:
        command_bus.handle(
            RegisterUser(
                CreateUser(
                    register_data.login,
                    register_data.email,
                    register_data.password
                )
            )
        )

        return {
            "message": None,
            "code": status.HTTP_201_CREATED
        }
    except LoginAlreadyTaken:
        response.status_code = status.HTTP_400_BAD_REQUEST

        return {
            "message": 'Login is already taken!',
            "code": status.HTTP_400_BAD_REQUEST
        }
