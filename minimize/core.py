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


class Minimize:
    """
    Minimize image(s) within a directory
    """

    def __init__(
        self,
        directory: str,
        name: str = None,
        size: typing.Tuple[int, int] = None,
        format: str = "PNG",
        replace: bool = False,
    ) -> None:
        _format = format.upper()
        assert os.path.isdir(
            directory
        ), f"{directory} does not exist. Recheck your directory path."

        assert (
            _format in IMAGE_FORMATS
        ), f"Image file format {_format} is not supported."

        if name is not None:
            assert os.path.isfile(f"{directory + name}"), f"File {name} does not exist."
            name = name.split(".")[0]
        self.dir = directory
        self.size = size
        self.replace = replace
        self.format = _format
        self.name = name

    def __call__(self) -> None:
        for image in self._images_of_dir():
            outfile = f"{self.dir}/{self.filename}-min.png"
            path = f"{self.dir}/{image}"
            if self.replace:
                outfile = path
            try:
                im = Image.open(path)
                im.thumbnail(self.size, Image.ANTIALIAS)
                im.save(outfile, self.format)
            except IOError as exc:
                click.echo(f"Cannot resize image {image}, {exc}")

    def _images_of_dir(self) -> typing.Generator[str, None, None]:
        for file in os.listdir(self.dir):
            self.filename = file.split(".")[0]
            if self.name is not None and self.name != self.filename:
                continue
            yield file
            if self.name is not None and self.name == self.filename:
                break
