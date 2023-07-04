
from src.modules.shared.application.messenger import Event


class UserRegistered(Event):
    def __init__(self, user_id: str, project_id: str):
        self._user_id = user_id
        self._project_id = project_id

    def get_user_id(self) -> str:
        return self._user_id

    def get_project_id(self) -> str:
        return self._project_id
