from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from gpucompare import version
from gpucompare.example import gpu_name


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="gpucompare",
    help="Compare GPUs",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]gpucompare[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(name="")
def main(
    name: str = typer.Option(..., help="GPU name to print."),
    color: Optional[Color] = typer.Option(
        None,
        "-c",
        "--color",
        "--colour",
        case_sensitive=False,
        help="Color for print. If not specified then choice will be random.",
    ),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the gpucompare package.",
    ),
) -> None:
    """Compare GPUs"""
    if color is None:
        color = choice(list(Color))

    greeting: str = gpu_name(name)
    console.print(f"[bold {color}]{greeting}[/]")


if __name__ == "__main__":
    app()
