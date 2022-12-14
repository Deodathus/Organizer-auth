
from fastapi import APIRouter, status, Depends
from dependency_injector.wiring import inject, Provide
from .requests import CreateProjectRequest, UpdateProjectRequest
from src.modules.project.application.queries import GetAllProjects
from src.modules.project.application.commands import StoreProject, DeleteProject, UpdateProject
from container import ApplicationContainer
from src.modules.shared.application.messanger import QueryBus, CommandBus

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


@router.delete('/project/{project_id}', status_code=status.HTTP_204_NO_CONTENT)
@inject
def delete_project(
        project_id: str,
        command_bus: CommandBus = Depends(
            Provide[ApplicationContainer.project.command_bus]
        )
) -> dict:
    command_bus.handle(
        DeleteProject(project_id)
    )

    return {
        "message": None,
        "code": status.HTTP_204_NO_CONTENT
    }


@router.patch('/project/{project_id}', status_code=status.HTTP_204_NO_CONTENT)
@inject
def update_project(
        project_id: str,
        request: UpdateProjectRequest,
        command_bus: CommandBus = Depends(
            Provide[ApplicationContainer.project.command_bus]
        )
) -> dict:
    command_bus.handle(
        UpdateProject(project_id, request.name)
    )

    return {
        "message": None,
        "code": status.HTTP_204_NO_CONTENT
    }
