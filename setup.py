from setuptools import setup

setup(
    name="minimize",
    version="0.1",
    py_modules=["cli", "minimize"],
    install_requires=["Click", "Pillow", "mypy"],
    entry_points="""
        [console_scripts]
        minimize=cli:run
    """,
)
