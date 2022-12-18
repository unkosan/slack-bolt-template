from src import Core
from slack_bolt import Say
from logging import Logger
from typing import Dict

import random
import re

@Core.app.message(re.compile(r"^dice", re.I))
def roll_dice(message: Dict, say: Say, logger: Logger):
    roll = random.randint(1, 6)
    say(f":game_die: {roll}")