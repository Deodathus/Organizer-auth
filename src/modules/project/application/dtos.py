

class ProjectsCollection(object):
    def __init__(self, projects: list):
        self.projects = projects

    def get(self) -> list:
        return self.projects
