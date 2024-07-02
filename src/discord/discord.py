from injector import inject
import requests


class Discord():
    @inject
    def __init__(self):
        print(f'Initializing {self.__class__.__name__}')

    def post_message_to_webhook(self, webhook_url: str, message: str) -> None:
        print(f'Posting message to {webhook_url}:\n{message}\n')
        data = {
            "content": message,
        }

        result = requests.post(webhook_url, json=data, timeout=20)
        assert str(result.status_code).startswith("2")
