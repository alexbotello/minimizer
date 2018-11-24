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
        _format = format.upper()
        assert os.path.isdir(
            directory
        ), f"{directory} does not exist. Recheck your directory path."

        if _format is not None:
            assert (
                _format in IMAGE_FORMATS
            ), f"Image file format {format} is not supported."

        if name is not None:
            assert os.path.isfile(f"{directory}/{name}"), f"File {name} does not exist."
        self.dir = directory
        self.size = size
        self.format = _format
        self.name = name

    def __call__(self) -> None:
        for image in self._images_of_dir():
            outfile, extension = self.fp.split(".")
            if self.format is not None:
                extension = self.format.lower()
            outfile = f"{outfile}.{extension}"

            try:
                im = Image.open(self.fp)
                im.thumbnail(self.size, Image.ANTIALIAS)
                im.save(outfile, self.format)
            except IOError as exc:
                click.echo(f"Cannot resize image {image}, {exc}")

    def _images_of_dir(self) -> typing.Generator[str, None, None]:
        for file in os.listdir(self.dir):
            self.fp = f"{self.dir}/{file}"
            if not os.path.isfile(self.fp):
                continue
            if self.name is not None and self.name != file:
                continue
            yield file
            if self.name is not None and self.name == file:
                break
