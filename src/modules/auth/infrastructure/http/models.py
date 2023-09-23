
from pydantic import BaseModel


class RegisterModel(BaseModel):
    login: str
    email: str
    password: str
    project_id: str


class AuthModel(BaseModel):
    login: str
    password: str
