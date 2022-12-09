
from fastapi import APIRouter, status
from .requests import CreateProjectRequest
from src.modules.project.infrastructure.repositories import MysqlProjectRepository

router = APIRouter()


@router.post('/project')
def store_project(request: CreateProjectRequest) -> dict:
    return {
        "message": request,
        "code": status.HTTP_200_OK
    }


@router.get('/project')
def get_all() -> dict:
    rep = MysqlProjectRepository()
    rep.get_all()

    return {
        "message": '',
        "code": status.HTTP_200_OK
    }
