from enum import Enum

from src.modules.shared.domain.value_objects import ID


class ProjectId(ID):
    pass


class ProjectOwnerId(ID):
    pass


class ProjectWebhookType(Enum):
    REGISTER = 1


class ProjectWebhookId(ID):
    pass


class ProjectWebhookUrl(object):
    _url: str

    def __init__(self, url: str):
        self._url = url

    def get_value(self) -> str:
        return self._url
