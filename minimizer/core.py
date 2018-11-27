import os
import typing

import click
import crayons
from PIL import Image


IMAGE_FORMATS = (
    "BMP",
    "EPS",
    "GIF",
    "ICNS",
    "IM",
    "JPEG",
    "MSP",
    "PCX",
    "PNG",
    "PPM",
    "SPIDER",
    "TIFF",
    "WebP",
    "XBM",
)


class Minimizer:
    """
    Minimize image(s) within a directory
    """

    def __init__(
        self,
        directory: str,
        name: str = None,
        size: typing.Tuple[int, int] = None,
        format: str = None,
    ) -> None:
        assert os.path.isdir(
            directory
        ), f"{directory} does not exist. Recheck your directory path."

        if format is not None:
            assert (
                format.upper() in IMAGE_FORMATS
            ), f"Image file format {format} is not supported."

        if name is not None:
            assert os.path.isfile(
                f"{directory}/{name}"
            ), f"File {crayons.red(name, bold=True)} does not exist."
        self.dir = directory
        self.size = size
        self.format = format
        self.name = name

    def __call__(self) -> None:
        for path, name, extension in self._images_of_dir():
            if self.format is not None:
                extension = f".{self.format.lower()}"
            outfile = f"{name}-min{extension}"
            try:
                im = Image.open(path)
                im.thumbnail(self.size, Image.ANTIALIAS)
                im.save(outfile, self.format)
            except IOError:
                filename = crayons.red(path.split("/")[-1], bold=True)
                click.echo(f"Cannot resize {filename}")

    def _images_of_dir(
        self
    ) -> typing.Generator[typing.Tuple[str, str, str], None, None]:
        for entry in os.scandir(self.dir):
            if not entry.is_file():
                continue  # pragma: no cover
            if self.name is not None and self.name != entry.name:
                continue  # pragma: no cover
            name, extension = os.path.splitext(entry.path)
            yield entry.path, name, extension
            if self.name is not None and self.name == entry.name:
                break  # pragma: no cover
