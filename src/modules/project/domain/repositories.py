
from .entities import Project, ProjectWebhook
from .value_objects import ProjectId, ProjectWebhookType


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

    def exists_by_id(self, project_id: ProjectId) -> bool:
        pass


class ProjectWebhookRepository:
    """ An interface to project webhook repository"""

    ...

    def store(self, webhook: ProjectWebhook) -> None:
        pass

    def get_by_project_id_and_type(self, project_id: ProjectId, webhook_type: ProjectWebhookType) -> ProjectWebhook:
        pass
