
import requests

from src.modules.project.application.services import UserWebhookRequestTriggererInterface \
    as UserWebhookRequestTriggererInterface
from src.modules.project.infrastructure.exceptions import WebhookRequestError


class UserWebhookRequestTriggerer(UserWebhookRequestTriggererInterface):
    def trigger(self, webhook_url: str, user_id: str) -> None:
        response = requests.post(
            webhook_url,
            json={"userId": f'{user_id}'}
        )

        if response.status_code is not 201:
            raise WebhookRequestError(
                f'Response code: {response.status_code}, Response error: {response.text}'
            )

