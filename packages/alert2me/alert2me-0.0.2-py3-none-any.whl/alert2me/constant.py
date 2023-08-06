import os
from pathlib import Path

ALERT2ME_CLI_PATH = Path(f"{os.getenv('HOME')}/.alert2me/usr/bin")
CONFIGURE_PATH = f"{os.getenv('HOME')}/.alert2me/usr/credential.json"
CONFIGURE_PATH = Path(os.getenv("CONFIGURE_PATH", CONFIGURE_PATH))

CONFIGURE_QUESTIONS = [
    {
        "type": "input",
        "name": "slack_key",
        "message": "What's your slack key?",
    },
    {
        "type": "input",
        "name": "user_id",
        "message": "What's your slack user id?",
    },
    {
        "type": "input",
        "name": "server_id",
        "message": "What's the server name(id) running the job?",
    },
]