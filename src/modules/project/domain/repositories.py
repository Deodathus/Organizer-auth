
from .entities import Project
from .value_objects import ProjectId


class ProjectRepository:
    """An interface to project repository"""

    ...

    def get_all(self) -> list:
        pass

    def store(self, project: Project) -> None:
        pass

    def delete(self, project_id: ProjectId) -> None:
        pass

    def update(self, project_id: ProjectId, project_name: str) -> None:
        pass


class ProjectOwnerRepository:
    """ An interface to project owner repository"""

    ...
