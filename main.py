
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from container import ApplicationContainer
from src.modules.auth.infrastructure.http import controllers as auth_routes
from src.modules.project.infrastructure.http import controllers as project_routes


def create_app() -> FastAPI:
    application = FastAPI()

    application.container = ApplicationContainer()
    application.include_router(auth_routes.router)
    application.include_router(project_routes.router)

    origins = [
        "http://localhost:3002",
        "http://127.0.0.1:3002",
        "https://auth.lil-develo.com"
    ]

    application.add_middleware(
        CORSMiddleware, 
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = create_app()
