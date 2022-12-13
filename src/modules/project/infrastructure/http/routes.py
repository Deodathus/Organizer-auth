
from fastapi import APIRouter, status, Depends
from dependency_injector.wiring import inject, Provide
from .requests import CreateProjectRequest
from src.modules.project.application.queries import GetAllProjects
from src.modules.project.application.commands import StoreProject
from container import ApplicationContainer
from src.modules.shared.application.messanger import QueryBus, CommandBus
from src.modules.project.application.dtos import ProjectDTO

router = APIRouter()


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


@router.post('/project', status_code=status.HTTP_201_CREATED)
@inject
def store_project(
        request: CreateProjectRequest,
        command_bus: CommandBus = Depends(
            Provide[ApplicationContainer.project.command_bus]
        )
) -> dict:
    command_bus.handle(
        StoreProject(request.name)
    )

    return {
        "message": None,
        "code": status.HTTP_201_CREATED
    }
