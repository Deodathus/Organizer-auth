
from fastapi import FastAPI
from container import ApplicationContainer
from src.modules.auth.infrastructure.http import routes as auth_routes
from src.modules.project.infrastructure.http import routes as project_routes


def create_app() -> FastAPI:
    application = FastAPI()

    application.container = ApplicationContainer()
    application.include_router(auth_routes.router)
    application.include_router(project_routes.router)

    return application


app = create_app()
