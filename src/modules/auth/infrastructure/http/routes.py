
from fastapi import APIRouter, status, Depends
from dependency_injector.wiring import inject, Provide
from container import ApplicationContainer
from .models import AuthModel, RegisterModel
from src.modules.shared.application.messanger import CommandBus
from src.modules.auth.application.commands import RegisterUser
from src.modules.auth.application.dtos import CreateUser

router = APIRouter()


@router.get('/')
@inject
def index(version: str = Provide[ApplicationContainer.config.api.version]):
    return {
        "message": f'Version: {version}',
        "code": status.HTTP_200_OK
    }


@router.post('/login')
def login(auth_data: AuthModel):
    return {
        "message": auth_data,
        "code": status.HTTP_200_OK
    }


@router.post('/user', status_code=status.HTTP_201_CREATED)
@inject
def register(
        register_data: RegisterModel,
        command_bus: CommandBus = Depends(Provide[ApplicationContainer.auth.command_bus])
) -> dict:
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
