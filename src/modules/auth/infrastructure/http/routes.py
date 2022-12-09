
from fastapi import APIRouter, status
from .models import AuthModel

router = APIRouter()


@router.post('/auth')
def auth(auth_data: AuthModel):
    return {
        "message": auth_data,
        "code": status.HTTP_200_OK
    }
