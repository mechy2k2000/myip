#! /usr/bin/python3

"""myip.py

Usage:
<<<<<<< HEAD
    myip.py [-havqd46] [-l PERIOD] [-T]
=======
    myip.py [-hvlq46]
>>>>>>> a1ca7c32f48686d1ea5e3d6365161c6ba94b5553

Options:

    -h --help       Show this screen
    -v --version    Show version
    -6 --six        Show the IPv6 address 
    -4 --four       Show the IPv4 address only
    -q --quiet      Return only the address
<<<<<<< HEAD
    -l --loop       Run in a loop
    -d --debug      Run in debug mode
    -T              Print timestamp  
    -a              Print arguments
=======
    -l --loop       Run in loop

>>>>>>> a1ca7c32f48686d1ea5e3d6365161c6ba94b5553
"""

from docopt import docopt
from getip import getip
<<<<<<< HEAD
import datetime
import time
import decimal

arguments = docopt(__doc__, version='0.0.1')

def loop(PERIOD):
    while quit is False:
        start = time.time()
        print("Start: " + time.strftime("%H:%M:%S"))
        print(getip())
        
        time.sleep(PERIOD)


# Run main 

#TODO arrange "if logic in a more sensible order i.e. -l maybe needs to be last"

if __name__ == "__main__":
    if arguments['-q'] is True:
        print(getip())
    
    elif arguments['-l'] is True:
        print("loop")  
        print("RUN IN A LOOP")
        print(decimal(arguments['PERIOD']))
        loop(arguments['PERIOD'])
       
    
    elif arguments['-d']:
        print("******** Debug MODE **********")
        print(arguments)
=======
from pyfile import pyfile


arguments = docopt(__doc__, version='0.0.1')

if arguments['-q'] is True:
    print(getip())
    exit(0)

print(arguments)

if arguments['-l'] is True:
    print("Loop")    
>>>>>>> a1ca7c32f48686d1ea5e3d6365161c6ba94b5553
    
    elif arguments['-T']:
        print('Timestamp')
    else: 
        print(getip())
        
