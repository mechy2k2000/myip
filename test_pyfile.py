#! /usr/bin/python3

"""test_pyfile.py

Usage:
    test_pyfile [-dh]FILE IP

Options:

    -h --help Show this screen
       
    -d 
"""

from lib.docopt import docopt

import pyfile

arguments = docopt(__doc__, version='0.0.0.0.1')

print(arguments)

pyfile.writeFile(arguments['FILE'], arguments['IP'])
