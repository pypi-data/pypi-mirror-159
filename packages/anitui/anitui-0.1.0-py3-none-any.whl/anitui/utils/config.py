import json
from pathlib import Path


def get_config():
    with open(f"{str(Path.home())}/.config/anitui/config.json", "r") as configfile:
        config = json.loads(configfile.read())
    return config
