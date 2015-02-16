import os
import sys

file = ('../log.log')
count = 0

for line in file:
    count = count + 1

print ("Line count in %s is %s" % (file, count)) 
