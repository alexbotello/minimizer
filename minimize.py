import os
import typing

import click
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


class MinimizeImages:
    """
    Minimize all images within a directory
    """

    def __init__(
        self,
        directory: str,
        dimensions: typing.Tuple[int, int] = None,
        format: str = "PNG",
    ) -> None:
        _format = format.upper()
        assert os.path.isdir(
            directory
        ), f"{directory} does not exist. Recheck your directory path."

        assert (
            _format in IMAGE_FORMATS
        ), f"Image file format {_format} is not supported"

        self.dir = directory
        self.dimensions = dimensions
        self.format = _format

    def __call__(self) -> None:
        for image in os.listdir(self.dir):
            name = image.split(".")[0]
            outfile = f"{name}-re"
            path = f"{self.dir}/{image}"
            try:
                im = Image.open(path)
                im.thumbnail(self.dimensions, Image.ANTIALIAS)
                im.save(outfile, self.format)
            except IOError as exc:
                click.echo(f"Cannot resize image {image}, {exc}")
