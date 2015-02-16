#! /usr/bin/python3

import datetime, time
import sys
sys.path.append("..")
from getip import getip

quit = False

def loop(PERIOD):
    while quit is False:
        start = time.time()
        print("Start: " + time.strftime("%H:%M:%S"))
        print(getip())
        
        time.sleep(PERIOD)



loop(1)

