
from __future__ import annotations

from .value_objects import ProjectId, ProjectOwnerId, ProjectWebhookType, ProjectWebhookUrl, ProjectWebhookId
import datetime


class ProjectWebhook(object):
    _project_webhook_id: ProjectWebhookId
    _project_id: ProjectId
    _type: ProjectWebhookType
    _url: ProjectWebhookUrl
    _active: bool

    def __init__(
        self,
        project_webhook_id: ProjectWebhookId,
        project_id: ProjectId,
        project_webhook_type: ProjectWebhookType,
        url: ProjectWebhookUrl,
        active: bool
    ):
        self._project_webhook_id = project_webhook_id
        self._project_id = project_id
        self._type = project_webhook_type
        self._url = url
        self._active = active

    @staticmethod
    def create(
        project_id: ProjectId,
        project_webhook_type: ProjectWebhookType,
        url: ProjectWebhookUrl
    ) -> ProjectWebhook:
        return ProjectWebhook(
            ProjectWebhookId.generate(),
            project_id,
            project_webhook_type,
            url,
            True
        )

    @staticmethod
    def reproduce(
        project_webhook_id: ProjectWebhookId,
        project_id: ProjectId,
        project_webhook_type: ProjectWebhookType,
        url: ProjectWebhookUrl,
        active: bool
    ) -> ProjectWebhook:
        return ProjectWebhook(
            project_webhook_id,
            project_id,
            project_webhook_type,
            url,
            active
        )

    def get_id(self) -> ProjectWebhookId:
        return self._project_webhook_id

    def get_project_id(self) -> ProjectId:
        return self._project_id

    def get_type(self) -> ProjectWebhookType:
        return self._type

    def get_url(self) -> ProjectWebhookUrl:
        return self._url

    def get_active(self) -> bool:
        return self._active


class ProjectOwner(object):
    _project_owner_id: ProjectOwnerId
    _name: str

    def __init__(self, project_owner_id: ProjectOwnerId, name: str):
        self._project_owner_id = project_owner_id
        self.name = name

    def __str__(self) -> str:
        return self._name

    def get_id(self) -> ProjectOwnerId:
        return self._project_owner_id

    def get_name(self) -> str:
        return self._name


class Project(object):
    _id: ProjectId
    _name: str
    _owner: ProjectOwnerId
    _created_at: datetime.datetime

    def __init__(self, project_id: ProjectId, name: str):
        self._id = project_id
        self._name = name

    def __str__(self) -> str:
        return str({
            "id": self._id.value,
            "name": self._name,
            "ownerId": self._owner.value
        })

    def get_id(self) -> ProjectId:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_owner(self) -> ProjectOwnerId:
        return self._owner

    def get_created_date(self) -> datetime.datetime:
        return self._created_at

