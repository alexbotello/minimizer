import os
import typing

import click

from minimize import Minimize


@click.command()
@click.option(
    "-d",
    "--dir",
    "directory",
    default=os.getcwd(),
    help="Specify directory to resize, will default to current directory",
)
@click.option(
    "-s",
    "--size",
    "size",
    type=(int, int),
    default=(250, 250),
    help="What size do you want your images? Example: 250 250",
)
@click.option(
    "-f",
    "--format",
    "format",
    default="PNG",
    help="What format would you like your images in? Defaults to PNG",
)
@click.option(
    "-n",
    "--name",
    "name",
    help="Name of specific image file to minimize. Must include file extension",
)
@click.option(
    "-r",
    "--replace",
    "replace",
    is_flag=True,
    help="Replace orginal files with new images",
)
def run(*args, **kwargs) -> None:
    mini = Minimize(*args, **kwargs)
    mini()
    click.echo(f"Minimization complete! \U0001F4AB")
