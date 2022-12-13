
from .dtos import ProjectsCollection
from src.modules.project.domain.repositories import ProjectRepository
from src.modules.shared.application.messanger import Query, QueryHandler


class GetAllProjects(Query):
    pass


class GetAllProjectsQueryHandler(QueryHandler):
    def __init__(self, project_repository: ProjectRepository):
        self._project_repository = project_repository

    def handle(self, query: GetAllProjects) -> ProjectsCollection:
        projects = self._project_repository.get_all()

        return ProjectsCollection(projects)
