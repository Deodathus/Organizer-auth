
from .dtos import ProjectsCollection
from src.modules.project.domain.repositories import ProjectRepository


class GetAllProjects(object):
    pass


class GetAllProjectsQueryHandler(object):
    def __init__(self, project_repository: ProjectRepository):
        self._project_repository = project_repository

    def handle(self, query: GetAllProjects) -> ProjectsCollection:
        projects = self._project_repository.get_all()

        return ProjectsCollection(projects)
