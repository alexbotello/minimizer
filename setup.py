import os
import re

from setuptools import setup

def get_version(module):
    init_py = open(os.path.join(module, "__init__.py")).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

def get_long_description():
    return open('README.md', 'r', encoding="utf8").read()

setup(
    name="minimizer",
    version=get_version("minimizer"),
    url="https://github.com/alexbotello/minimizer",
    license="MIT",
    description="A command line tool to shrink image(s) in a directory to a specified size",
    long_description=get_long_description(),
    author="Alexander Botello",
    author_email="alexander.botello@g.austincc.edu",
    py_modules=["minimizer"],
    install_requires=["Click", "Pillow"],
    entry_points="""
        [console_scripts]
        minimizer=minimizer.cli:run
    """,
)
