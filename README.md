<a href="https://travis-ci.org/alexbotello/minimizer">
    <img src="https://travis-ci.org/alexbotello/minimizer.svg?branch=master" alt="Build Status">
</a>
<a href="https://codecov.io/gh/alexbotello/minimizer">
    <img src="https://codecov.io/gh/alexbotello/minimizer/branch/master/graph/badge.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/minimizer/">
    <img src="https://badge.fury.io/py/minimizer.svg" alt="PyPI version">
</a>

# minimizer
A command line tool that shrinks images in a directory to a specified size

Installation
-------
Install using pip:
```
pip install minimizer
```
Or with pipenv:
```
pipenv install minimizer
```

Usage
-------

    $ minimizer
    Usage: minimizer [OPTIONS]

    Options:
      -d, --dir        Specify path for directory. Defaults to current working directory.
      -s, --size       Specify new size dimensions. Defaults to 250 250
      -f, --format     Specify image format.
      -n, --name       Name specific image file to minimize. Must include file extension.
      --help           Show this message and exit.


    Usage Examples:
       Minimize all images in current directory using defaults:
       $ minimizer

       Minimize all images in current directory to a new size:
       $ minimizer -s 75 50

       Minimize all images to a new size and format in a specified directory:
       $ minimizer -d /home/user/code/images -s 125 50 -f jpeg

       Minimize a specific image in current directory:
       $ minimizer -n img12.jpg -s 150 150

       Minimize a specfic image in another directory:
       $ minimizer -d /home/user/code/images -n img12.jpg -s 200 100
