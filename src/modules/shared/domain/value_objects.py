
from __future__ import annotations
import uuid


class ID(object):
    value: uuid.UUID

    def __init__(self, value: uuid.UUID):
        self.value = value

    @staticmethod
    def from_string(string_id: str):
        return ID(uuid.UUID(string_id))

    @staticmethod
    def generate():
        return ID(uuid.uuid4())
