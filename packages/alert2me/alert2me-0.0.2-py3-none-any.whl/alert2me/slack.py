from typing import List, Optional
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from .configure import get_configure
from .constant import CONFIGURE_PATH

class SlackClient:
    def __init__(
        self,
    ):
        config = get_configure()
        slack_key = config.get("slack_key", None)
        user_id = config.get("user_id", None)
        server_id = config.get("server_id", None)
        assert slack_key is not None
        assert user_id is not None
        self.client = WebClient(token=slack_key)
        self.user_id = user_id
        self.server_id = server_id

    def __call__(
        self,
        message: str,
    ):
        try:
            response = self.send_message(message)
        except SlackApiError as e:
            print(e)

    def send_message(self, message):
        response = self.client.chat_postMessage(
            channel=self.user_id,
            text=message
        )
        return response