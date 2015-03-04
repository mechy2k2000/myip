"""
this is a test of using sqlite to store ip entries
note considering using "log.log" to goes to distro's log location
the db will be stored somewhere in the distro

"""


import sqlite3


conn = sqlite3.connect('testdb')

tlbcmd = 'create table db_log (ip char(15), date char(10), time char(12))'

curs = conn.cursor()
try:
    curs.execute(tlbcmd)
except sqlite3.OperationalError:
    print("Database created")

curs.execute('insert into db_log values (?, ?, ?)', ('2.2.2.2', '0001-01-01', '01:01:01,001'))

conn.commit()
