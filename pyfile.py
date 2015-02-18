"""
This is suppose to write and read to the flat file "log",
Note that the "log"  file is in the same directory for right now

"""



import logging
import os
  
       

def __init__(self, name, filepath):
    self.name = name
    self.file = filepath
    self.cwd = os.getcwd()
    self.lastline = 0
    self.firstline = 0
    self.linecount = 0

def getlastlinecount(file):
    count = 0
    try:
        for line in file:
            count = count + 1
        return count
    except:         #TODO have the proper exceptions returned  
        Print("Something happen returning the last line count")
        
def getlastline(file):
        
     # Gets the line count for the log.log file and sets the varible
     # self.linecount
    linecount = 0
    try:
            
        file = open(file)
        count = 0
        for line in file:
            count = count + 1
        linecount = count
        print("line count: %s" % linecount)
    except:
        print('something happen while getting a line count from %s' % file)   
    
        
def writeFile(file, ip, debug=False):
    """
    writeFile is the method to write to the log file using python's logger 
    give the method self for variables, ip for the ip to write to, and 
    debug verbose about what its doing
    """

    
    logging.basicConfig(filename='log.log', level=logging.DEBUG, 
                        format='%(levelname)s %(asctime)s %(message)s') 
    
    print(ip)
    
    
    
    try:
        if ip :
            
            if debug == True:                                            #
                print('Debug mode: writeFILE called writing to file!!') 
                print("Current Working Directory: %s"  % os.getcwd())
                print("IP variable being passed:: %s" % ip)
                logging.debug('writeFile called, writing to log now')

            logging.info(ip) 
            try:
                getlastline(debug=True)
            except Exception as e:  
                print("Error!!({0}):  ".format(e.errno, e.strerror))
        else:
            print("Something went wrong ({0}): {1}".format(e.errno, e.strerror))
    
    except Exception as e:
        print('the ip address is needed!!' + "Exception: " ) #TODO return the string of the error 
        if debug == True: 
            logging.debug("writeFile was called threw an exception ({0}): {1}".format(e.errno, e.strerror))
    
    
def readFile(file):
    
    """
    readFile reads the log file and returns value
    """

 
# if __name__ == '__main__':
#     print('Running as a main')        
 

