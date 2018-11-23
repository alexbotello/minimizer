import os
import typing

import click

from minimize import MinimizeImages


@click.command()
@click.option(
    "--dir",
    default=os.getcwd(),
    help="Specify directory to resize, will default to current directory",
)
@click.option(
    "--size",
    default=(250, 250),
    help="What size do you want your images? Example: 250 250",
)
@click.option(
    "--format",
    default="PNG",
    help="What format would you like your images in? Defaults to PNG",
)
def run(dir: str, size: typing.Tuple[int, int], format: str) -> None:
    mini = MinimizeImages(dir, size, format)
    mini()
    click.echo(f"All images have been minimized \U0001F4AB")
