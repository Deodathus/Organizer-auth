
from .entities import Project


class ProjectRepository:
    """An interface to project repository"""

    ...

    def get_all(self) -> list:
        pass

    def store(self, project: Project) -> None:
        pass


class ProjectOwnerRepository:
    """ An interface to project owner repository"""

    ...
