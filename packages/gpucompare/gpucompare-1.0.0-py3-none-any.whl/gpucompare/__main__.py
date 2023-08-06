from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from gpucompare import version
from gpucompare.parse import parse_csv


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
    csv_data: str = typer.Option(
        ...,
        help="""CSV file containing row-wise GPU data

            \b 
            Possible columns:
            gpu_name (str): name of gpu  [required]
            architecture (str): GPU architecture
            cuda_cores (int): number of cuda cores
            fp32_perf (float): fp32 performance in TFLOPS
            fp16_perf (float): fp16 performance in TFLOPS
            int8_perf (float): int8 performance in TOPS
            mem (float): gpu memory in GiB
            mem_bandwidth (float): memory bandwidth in GB/s
            """,
    ),
    # color: Optional[Color] = typer.Option(
    #     None,
    #     "-c",
    #     "--color",
    #     "--colour",
    #     case_sensitive=False,
    #     help="Color for print. If not specified then choice will be random.",
    # ),
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
    # if color is None:
    color = choice(list(Color))

    output: str = parse_csv(csv_data)
    console.print(f"[bold {color}]{output}[/]")


if __name__ == "__main__":
    app()
