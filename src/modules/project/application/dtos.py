
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
