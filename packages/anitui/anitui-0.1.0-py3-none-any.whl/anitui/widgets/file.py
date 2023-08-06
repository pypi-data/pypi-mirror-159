from rich.align import Align
from rich.panel import Panel
from rich.style import StyleType
from rich.console import Console, ConsoleOptions, RenderResult, RenderableType
from rich.table import Table
from textual.widgets import ButtonPressed
from textual.widget import Widget
from textual.reactive import Reactive
from textual import events


class FileRenderable:
    def __init__(self, label: RenderableType, style: StyleType = "") -> None:
        self.label = label
        self.style = style

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        width = options.max_width
        height = options.max_height or 1

        yield Align.center(
            self.label, vertical="middle", style=self.style, width=width, height=height
        )


class File(Widget):
    def __init__(
        self,
        label: RenderableType,
        name: str | None = None,
        style: StyleType = "white on dark_blue",
    ):
        super().__init__(name=name)
        self.name = name or str(label)
        self.button_style = style

        self.label = label

    label: Reactive[RenderableType] = Reactive("")

    def render(self) -> Panel:
        return FileRenderable(self.label, style=self.button_style)

    async def on_click(self, event: events.Click) -> None:
        event.prevent_default().stop()
        await self.emit(ButtonPressed(self))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False
