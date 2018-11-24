import os
import typing

import click

from minimizer.core import Minimizer


@click.command()
@click.option(
    "-d",
    "--dir",
    "directory",
    default=os.getcwd(),
    help="Specify path for directory. Defaults to current working directory",
)
@click.option(
    "-s",
    "--size",
    "size",
    type=(int, int),
    default=(250, 250),
    help="Specify new size dimensions. Defaults to 250 250",
)
@click.option(
    "-f",
    "--format",
    "format",
    default=None,
    help="Specifiy image format. Default image format is PNG",
)
@click.option(
    "-n",
    "--name",
    "name",
    help="Name specific image file to minimize. Must include file extension",
)
def run(*args: typing.Any, **kwargs: typing.Any) -> None:
    try:
        mini = Minimizer(*args, **kwargs)
        mini()
    finally:
        click.echo(f"Minimization complete! \U0001F4AB")
