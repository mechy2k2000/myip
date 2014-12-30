"""myip.py

Usage:
    myip.py [-hvq46]

Options:

    -h --help       Show this screen
    -v --version    Show version
    -6 --six        Show the IPv6 address 
    -4 --four       Show the IPv4 address only
    -q --quiet      Return only the address

"""

from lib.docopt import docopt
from getip import getip


arguments = docopt(__doc__, version='0.0.1')

if arguments['-q'] is True:
    print(getip())

if arguments['-l'] is True:
    
    
