"""myip.py

Usage:
    myip.py [-hvlq46]

Options:

    -h --help       Show this screen
    -v --version    Show version
    -6 --six        Show the IPv6 address 
    -4 --four       Show the IPv4 address only
    -q --quiet      Return only the address
    -l --loop       Run in loop

"""

from docopt import docopt
from getip import getip
from pyfile import pyfile


arguments = docopt(__doc__, version='0.0.1')

if arguments['-q'] is True:
    print(getip())
    exit(0)

print(arguments)

if arguments['-l'] is True:
    print("Loop")    
    
