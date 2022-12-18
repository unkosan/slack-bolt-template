from src import Core
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os

if __name__ == "__main__":
    SocketModeHandler(
        app = Core.app, 
        app_token = os.environ["SLACK_APP_TOKEN"],
    ).start()