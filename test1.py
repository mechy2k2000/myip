#! /usr/bin/python3

import sys
import argparse

from pyfile import writeFile
from pyfile import getlastline
from getip  import getip
from lib.docopt import docopt

"""testing
Usage:

    test.py [-hv STRING]

Options:

    -h, --help  Show this screen
    --version   Show version

"""

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.01.0')
    print(arguments)


