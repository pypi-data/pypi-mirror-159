from .browse import AniTUI
from .utils import config_exists, create_config
from pathlib import Path
import os


def main():
    if not config_exists():
        anime_dir = os.path.expanduser(input("Where is your Anime directory? [~/Videos/anime/]: "))
        anilist_username = input("What is your Anilist username? [blank] ")
        script_path = input("What is the path to your vlc-ani-discord script? [blank] ")
        create_config(config={
            "anime_dir": anime_dir if anime_dir else f"{str(Path.home())}/Videos/anime",
            "script_path": script_path,
            "anilist_username": anilist_username
        })

    AniTUI.run(title="Anime TUI", log="textual.log")
