#! /usr/bin/python3


"""
Usage:

    test.py ship new NAME
    test.py ship 

Options:
    -v --version    Show the version
    -h --help       Show the help
    

"""

from lib.docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.01.0')
    print(arguments)


