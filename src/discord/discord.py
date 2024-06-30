from injector import inject
import requests


class Discord():
    @inject
    def __init__(self):
        print(f'Initializing {self.__class__.__name__}')

    def post_message_to_webhook(self, webhook_url: str, message: str) -> None:
        print(f'Posting message to {webhook_url}: {message}')
        data = {
            "content": message,
        }

        result = requests.post(webhook_url, json=data, timeout=20)
        assert str(result.status_code).startswith("2")
        print(f'Message posted successfully to {webhook_url}')
