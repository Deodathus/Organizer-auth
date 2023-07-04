
import datetime


class ProjectDTO(object):
    def __init__(self, project_id: str, name: str, created_at: datetime.datetime):
        self.project_id = project_id
        self.name = name
        self.created_at = created_at


class ProjectsCollection(object):
    def __init__(self, projects: list):
        self.projects = projects

    def get(self) -> list:
        return self.projects


class ProjectWebhookToStore(object):
    _project_id: str
    _type: str
    _url: str

    def __init__(self, project_id: str, webhook_type: str, url: str):
        self._project_id = project_id
        self._type = webhook_type
        self._url = url

    def get_project_id(self) -> str:
        return self._project_id

    def get_type(self) -> str:
        return self._type

    def get_url(self) -> str:
        return self._url
