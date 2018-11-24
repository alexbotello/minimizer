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
        format: str = "PNG",
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
        self.format = _format
        self.name = name

    def __call__(self) -> None:
        for image in self._images_of_dir():
            fp = f"{self.dir}/{image}"
            outfile = f"{fp.split('.')[0]}.{self.format.lower()}"
            try:
                im = Image.open(fp)
                im.thumbnail(self.size, Image.ANTIALIAS)
                im.save(outfile, self.format)
            except IOError as exc:
                click.echo(f"Cannot resize image {image}, {exc}")

    def _images_of_dir(self) -> typing.Generator[str, None, None]:
        for file in os.listdir(self.dir):
            filename = file.split(".")[0]
            if not os.path.isfile(file):
                continue
            if self.name is not None and self.name != filename:
                continue
            yield file
            if self.name is not None and self.name == filename:
                break
