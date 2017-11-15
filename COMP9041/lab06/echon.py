#!/usr/bin/env python

# repeat echo in python

import sys,re

if len(sys.argv) != 3: # echon.py is included
    # sys.stderr.write("Usage: ./echon.py <number of lines> <string>")
    # print sys.stderr
    print "Usage: ./echon.py <number of lines> <string>"
    exit(1)

pattern = "^[0-9]+$"

if not re.match(pattern, sys.argv[1]):
    # sys.stderr.write("./echon.py: argument 1 must be a non-negative integer")
    print "./echon.py: argument 1 must be a non-negative integer"
    exit(1)
    
for i in range(int(sys.argv[1])):
    print sys.argv[2]
