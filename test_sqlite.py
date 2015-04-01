"""
this is a test of using sqlite to store ip entries
note considering using "log.log" to goes to distro's log location
the db will be stored somewhere in the distro

"""


import sqlite3
import sys
import re


conn = sqlite3.connect('testdb')

#tlbcmd = 'create table db_log (ip char(15), date char(10), time char(12))'

curs = conn.cursor()

#try:    
#    curs.execute(tlbcmd)
#except sqlite3.OperationalError:
#   print("Database already created")

#curs.execute('insert into db_log values (?, ?, ?)', ('2.2.2.2', '0001-01-01', '01:01:01,001'))

def returnNumOfUniqueIP():
    # use this as a template for other stat return functions

    num_ip = 0;
    try:
        curs.execute('select Count(*) from unique_ip')

        for row in curs.fetchall():
            result = row
            num_ip = str(result).strip('(\',)')
            
    except:
        print("Error while getting count of UniqueIP")
        
    return num_ip
    
def checkUniqueIP(target_ip):
    # this function checks database to see if target ip is unique
    # if this is true it will add to database

    try:
        cmd = "select ip from unique_ip where ip = '" + target_ip + "'"
        result = curs.execute(cmd)
        print(len(result))
    except:
        print("Error Something happened while Checking unique_ip")
    
    for row in curs.fetchall():
        print(row)

def getTSLC():
# Get the timestamp for when the IP was last changed
    try:
        cmd = "select time_change from variables;"
        result = curs.execute(cmd)
        for row in curs.fetchall():
            print(str(row).strip('(\',)')) 
    
    except Exception as e:
        print("Error something happened while getting time since last change variable")
        print(str(e))

def setTSLC():
# Sets the timestamp for when the IP last changed

    try:
        cmd = "update variables set time_change=datetime(CURRENT_TIMESTAMP, 'localtime');"
        curs.execute(cmd)

    except Exception as e:
        print("Error something happened while setting time since last")
        print(str(e))
        
def getDefaultURL():
# Gets the default URL used to get the external IP
    
    try:
        cmd = "select default_url from variables;"
        result = curs.execute(cmd)
        for row in curs.fetchall():
            print(str(row).strip('(\',)'))
    except Exception as e:
        print("Error Something happened while getting the default URL variable")
        print(str(e))

def setDefaultURL(url):
# Sets the default URL used to get the external IP
    if url != None:
        url = "http://checkip.amazonaws.com"

    try:
        cmd = "update variables set default_url='" + url 
        result = curs.execute(cmd)
        for row in curs.fetchall():
            print(str(row).strip('(\',)'))

    except Exception as e:
        print("Error something happened while getting the default URL variable")
        print(str(e)) 

def returnNumOfAttemptLog():
    # use this as a template for other stat return functions

    num_attempts = 0


    try:
        curs.execute('select Count(*) from attempt_log')

        for row in curs.fetchall():
            result = row
            num_attempts = str(result).strip('(\',)')
            
    except Exception as e:
        print("Error while getting count of attempts from attempt_log")
        print(str(e))

    return num_attempts

def insertAttemptLog(outcome, url):
# add an attemptlog to the database
        
    values = {'outcome': outcome, 'url': url}

    if outcome is not'Fail' or outcome is not 'Success':
        try:
            raise TypeError
        except Exception as e:       
            print('Check your arguments')
    
    try:
        cmd = "insert into attempt_log(outcome, timestamp, attempted_url) values( %(outcome)s, datetime(CURRENT_TIMESTAMP, 'localtime'), %(url)s)" % values        
        print("trying to excute cmd")
        curs.execute(cmd) 
    except Exception as e:
        print("Error something has happen while adding an Attempt log to the database")
        print(str(e))
    

def returnNumOfErrorLog():
    # use this as a template for other stat return functions

    num_error = 0


    try:
        curs.execute('select Count(*) from error_log')

        for row in curs.fetchall():
            result = row
            num_error = str(result).strip('(\',)')
            
    except Exception as e:
        print("Error while getting count of error from error_log")
        print(str(e))

    return num_error

def insertErrorLog(error, url):
# add an attemptlog to the database
    values = {'error': error, 'url': url} 

    if error is None:
        try:
            raise TypeError
        except Exception as e:       
            print('Check your arguments')
    
    try:
        cmd = "insert into error_log(error, timestamp, attempted_url) values( %(error)s, datetime(CURRENT_TIMESTAMP, 'localtime'), %(url)s)" % values        
        print("trying to excute cmd")
        curs.execute(cmd) 
    except Exception as e:
        print("Error something has happen while adding an error log to the database")
        print(str(e))
 
            



insertErrorLog("'hello'", "'helo'")

# remember to have conn.commit 
conn.commit()
