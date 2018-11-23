# minimize
A command line tool that shrinks all images in a directory to a specified size

Usage
-------

    $ minimize
    Usage: minimize [OPTIONS]

    Options:
      --dir        Specify path for directory. Defaults to current working directory.
      --size       Specify new size dimensions. Defaults to 250 250
      --format     Specify image format. Default image format is PNG.
      --help       Show this message and exit.


    Usage Examples:
       Minimize all images in current directory using defaults:
       $ minimize

       Minimize all images in current directory to a new size:
       $ minimize --size 75 50

       Minimize all images to a new size and format in a specified directory:
       $ minimize --dir /home/user/code/images --size 125 50 --format JPEG
