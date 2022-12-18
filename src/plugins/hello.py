from src import Core
from slack_bolt import Say
from logging import Logger
from typing import Dict

import re

@Core.app.message(re.compile(r"^h(i|ello)", re.I))
def message_hello(message: Dict, say: Say, logger: Logger):
    say(f"Hey there!")