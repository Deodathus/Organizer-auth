from fastapi import FastAPI, status
from dependency_injector import containers, providers
from src.modules.auth.infrastructure.http import routes as auth_routes
from src.modules.project.infrastructure.http import routes as project_routes


class Container(object):
    wiring_config = containers.WiringConfiguration()


def create_app() -> FastAPI:
    application = FastAPI()

    application.container = Container()
    application.include_router(auth_routes.router)
    application.include_router(project_routes.router)

    return application


app = create_app()


@app.get("/")
async def root():
    return {
        "message": "Auth api.",
        "code": status.HTTP_200_OK,
    }
