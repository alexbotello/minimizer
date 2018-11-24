# minimizer
A command line tool that shrinks images in a directory to a specified size

## Installation
-------
Install using pip:
```
pip install minimizer
```
Or with pipenv:
```
pipenv install minimizer
```

## Usage
-------

    $ minimizer
    Usage: minimizer [OPTIONS]

    Options:
      -d, --dir        Specify path for directory. Defaults to current working directory.
      -s, --size       Specify new size dimensions. Defaults to 250 250
      -f, --format     Specify image format. Default image format is PNG.
      -n, --name       Name specific image file to minimize. Must include file extension.
      --help           Show this message and exit.


    Usage Examples:
       Minimize all images in current directory using defaults:
       $ minimizer

       Minimize all images in current directory to a new size:
       $ minimizer -s 75 50

       Minimize all images to a new size and format in a specified directory:
       $ minimizer -d /home/user/code/images --size 125 50 --format JPEG

       Minimize a specific image in current directory:
       $ minimizer -n img12.jpg -s 150 150
