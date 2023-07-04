
from pydantic import BaseModel


class CreateProjectRequest(BaseModel):
    name: str


class UpdateProjectRequest(BaseModel):
    name: str


class StoreProjectWebhookRequest(BaseModel):
    url: str
    type: str

