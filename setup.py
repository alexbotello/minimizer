import setuptools


def get_long_description():
    return open("README.md", "r", encoding="utf8").read()


setuptools.setup(
    name="minimizer",
    version="0.4.5",
    url="https://github.com/alexbotello/minimizer",
    license="MIT",
    description="A command line tool to shrink image(s) in a directory to a specified size",
    long_description=get_long_description(),
    author="Alexander Botello",
    author_email="alexander.botello@g.austincc.edu",
    packages=setuptools.find_packages(),
    py_modules=["minimizer"],
    install_requires=["click", "pillow", "crayons"],
    entry_points="""
        [console_scripts]
        minimizer=minimizer.cli:run
    """,
)
