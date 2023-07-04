

class UserWebhookRequestTriggererInterface(object):
    def trigger(self, webhook_url: str, user_id: str) -> None:
        pass
