import os
import sys

file = open('../log.log')

count = 0

for line in file:
    count = count + 1


print ("File name: %s" % file.name)  
print ("Line count in %s is %s" % (file, count)) 
