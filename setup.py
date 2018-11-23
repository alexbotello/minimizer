import os
import re

from setuptools import setup

def get_version(module):
    init_py = open(os.path.join(module. "__init__.py")).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

setup(
    name="minimize",
    version=get_version("minimize")
    py_modules=["minimize"],
    install_requires=["Click", "Pillow"],
    entry_points="""
        [console_scripts]
        minimize=cli:run
    """,
)
