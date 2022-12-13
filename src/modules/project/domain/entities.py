
from .value_objects import ProjectId, ProjectOwnerId
import datetime


class ProjectOwner(object):
    _id: ProjectOwnerId
    _name: str

    def __init__(self, id: ProjectOwnerId, name: str):
        self._id = id
        self.name = name

    def __str__(self) -> str:
        return self._name

    def get_id(self) -> ProjectOwnerId:
        return self._id

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

