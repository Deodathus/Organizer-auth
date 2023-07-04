
import requests

from src.modules.project.application.services import UserWebhookRequestTriggererInterface \
    as UserWebhookRequestTriggererInterface


class UserWebhookRequestTriggerer(UserWebhookRequestTriggererInterface):
    def trigger(self, webhook_url: str, user_id: str) -> None:
        requests.post(
            webhook_url,
            {
                "userId": user_id,
            }
        )
