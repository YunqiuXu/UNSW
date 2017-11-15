#!/usr/bin/python

import sys
print len(sys.argv)
print sys.argv

print "The file we need to open is {}".format(sys.argv[1])
with open(sys.argv[1],'r') as f:
    for line in f.readlines():
        print "Current line : {}".format(line[:-1]) # remove "\n"
