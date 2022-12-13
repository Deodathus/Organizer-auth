
from fastapi import APIRouter, status, Depends
from dependency_injector.wiring import inject, Provide
from .requests import CreateProjectRequest
from src.modules.project.application.queries import GetAllProjects
from container import ApplicationContainer
from src.modules.shared.application.messanger import QueryBus

router = APIRouter()


@router.post('/project')
def store_project(request: CreateProjectRequest) -> dict:
    return {
        "message": request,
        "code": status.HTTP_200_OK
    }


@router.get('/project')
@inject
def get_all(
        query_bus: QueryBus = Depends(
            Provide[ApplicationContainer.project.query_bus]
        )
) -> dict:
    return {
        "message": query_bus.handle(GetAllProjects()),
        "code": status.HTTP_200_OK
    }
