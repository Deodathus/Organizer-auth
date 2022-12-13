
from fastapi import APIRouter, status
from dependency_injector.wiring import inject, Provide
from container import ApplicationContainer
from .models import AuthModel

router = APIRouter()


@router.get('/')
@inject
def index(version: str = Provide[ApplicationContainer.config.api.version]):
    return {
        "message": f'Version: {version}',
        "code": status.HTTP_200_OK
    }


@router.post('/auth')
def auth(auth_data: AuthModel):
    return {
        "message": auth_data,
        "code": status.HTTP_200_OK
    }
