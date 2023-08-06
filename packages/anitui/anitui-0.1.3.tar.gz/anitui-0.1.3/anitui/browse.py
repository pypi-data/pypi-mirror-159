import os
from math import ceil
import subprocess
import sys

from rich.markdown import Markdown
from rich.console import Console, ConsoleOptions, RenderResult, RenderableType
from rich.panel import Panel
from rich.style import StyleType
from rich.align import Align
from rich.table import Table

from textual import events
from textual.app import App, DockLayout
from textual.widgets import (
    Footer,
    Placeholder,
    ScrollView,
    Button,
    ButtonPressed,
)
from textual.reactive import Reactive
from textual.widget import Widget

from .widgets import File, TableWidget, Header, Progress
from .utils import get_config, query_watch_list, check_valid_select, Parser



class AniTUI(App):
    filetypes = [".mp4", ".mkv"]
    selected = 0
    open_dir = []

    async def on_load(self, event: events.Load) -> None:
        """Bind keys with the app loads (but before entering application mode)"""
        await self.bind("q", "quit", "Quit")
        await self.bind("escape", "quit", "Quit")
        await self.bind("u", "back()", "Go back")
        self.config = get_config()
        self.dir = self.config["anime_dir"]
        self.script_path = self.config["script_path"]
        self.watch_list = query_watch_list(self.config['anilist_username']) if self.config['anilist_username'] else []
        self.offset = 0

    async def on_mount(self, event: events.Mount) -> None:
        """Create and dock the widgets."""
        await self.load_buttons()

    async def action_back(self):
        parent_dir = os.path.abspath(os.path.join(self.dir, os.pardir))
        await self.change_dir(parent_dir)

    def read_dir(self) -> [os.DirEntry]:
        open_dir = []
        with os.scandir(self.dir) as it:
            for entry in it:
                if (
                    entry.is_file() and any(ext in entry.name for ext in self.filetypes)
                ) or entry.is_dir():
                    open_dir.append(entry)
        open_dir.sort(key=lambda file: file.name)
        return open_dir

    def calculate_offset(self):
        # If at top, go up
        if self.offset >= self.selected:
            self.offset = self.selected
        # If at bottom, go down
        while not check_valid_select(self.file_names, self.selected, self.offset):
            self.offset += 1

    async def load_buttons(self) -> None:
        self.open_dir = self.read_dir()
        self.file_names = list(
            map(lambda file: self.parse_row(file.name), self.open_dir)
        )
        self.calculate_offset()
        await self.clear_buttons()
        await self.view.dock(
            TableWidget(rows=self.open_dir, file_names=self.file_names, style="white", selected=self.selected, offset=self.offset),
            edge="left",
        )

    async def clear_buttons(self) -> None:
        self.view.layout.docks.clear()
        self.view.widgets.clear()
        await self.view.dock(Header("Anime TUI"), edge="top")
        await self.view.dock(Progress(watch_list=self.watch_list), edge="right", size=Console().width // 3)
        await self.view.dock(Footer(), edge="bottom")

    async def change_dir(self, new_dir) -> None:
        self.selected = 0
        self.dir = new_dir
        await self.load_buttons()

    def parse_row(self, name):
        parser = Parser()
        return parser.parse(name)

    def open_anime(self, file) -> None:
        if sys.platform == 'win32':
            os.startfile(file)
            if self.script_path:
                os.startfile(self.script_path)
        else:
            subprocess.call(["vlc", file])
            if self.script_path:
                subprocess.call([self.script_path])


    async def handle_click(self, file) -> None:
        print(file)
        child = f"{self.dir}/{file}"
        if any(ext in file for ext in self.filetypes):
            self.open_anime(child)
            return
        await self.change_dir(child)

    async def handle_button_pressed(self, message: ButtonPressed) -> None:
        await self.handle_click(message.sender.name)

    async def increment(self):
        if self.selected + 1 < len(self.open_dir):
            self.selected += 1
        await self.load_buttons()

    async def decrement(self):
        if self.selected - 1 >= 0:
            self.selected -= 1
        await self.load_buttons()

    async def on_key(self, event) -> None:
        if event.key == "down" or event.key == "j":
            await self.increment()
        elif event.key == "up" or event.key == "k":
            await self.decrement()
        elif event.key == "enter":
            await self.handle_click(self.open_dir[self.selected].name)


#AniTUI.run(title="Anime TUI", log="textual.log")
