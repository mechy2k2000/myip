import socket
import urllib
import re
import time
import sys
from urllib.request import urlopen

"""
    IP functions that gets and return IPV4 addresses
"""


    
    #def __init__(self):
    #    self.ip = None
    #    self.target_url = None
        
def getip( url="http://checkip.amazonaws.com"):
    try:
        target_url = url
        #print(target_url)
        remotefile = urlopen(url).read()
            
        #print(remotefile)
        theIP = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", remotefile.decode())

        cleanip = str(theIP).strip('[\']')
        #print("your IP Address is: %s" %  cleanip)

        #self.ip = theIP
        #self.target_url = url
        return cleanip
    except IOError as err:
        print("Unable to connect to %s  {0}" % url)

        # TODO clean it up and add some more error handling and input validation
            


#if __name__ == "__main__":
#    print("Running as Main ")
#    test_ip = IP() 
#    test_ip.getip()   

    


    
    
     
