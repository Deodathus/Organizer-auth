
from __future__ import annotations


class WebhookRequestError(Exception):
    @staticmethod
    def create_with_message(message: str) -> WebhookRequestError:
        return WebhookRequestError(message)
