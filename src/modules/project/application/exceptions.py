
from __future__ import annotations


class InvalidWebhookType(Exception):
    @staticmethod
    def with_value(value: str) -> InvalidWebhookType:
        return InvalidWebhookType(value)


class ProjectDoesNotExist(Exception):
    @staticmethod
    def with_id(project_id: str) -> ProjectDoesNotExist:
        return ProjectDoesNotExist(project_id)
