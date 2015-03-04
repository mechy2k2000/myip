#! /usr/bin/python3

"""myip.py

Usage:
    myip.py [-havqd46] [-l PERIOD] [-T]

Options:

    -h --help       Show this screen
    -v --version    Show version
    -6 --six        Show the IPv6 address 
    -4 --four       Show the IPv4 address only
    -q --quiet      Return only the address
    -l --loop       Run in a loop
    -d --debug      Run in debug mode
    -T              Print timestamp  
    -a              Print arguments
"""

from lib.docopt import docopt
from getip import getip
import datetime
import time
import decimal
import pyfile


arguments = docopt(__doc__, version='0.0.1')

def loop(PERIOD):
    while quit is False:
        start = time.time()
        print("Start: " + time.strftime("%H:%M:%S"))
        print(getip())
        
        time.sleep(PERIOD)


# Run main 

#TODO arrange "if logic in a more sensible order i.e. -l maybe needs to be last"
file = "log.log"

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
        pyfile.writeFile(file,getip())
    
    elif arguments['-T']:
        print("Timestamp: " + time.strftime("%H:%M:%S"))
    else: 
        print(getip())
        
