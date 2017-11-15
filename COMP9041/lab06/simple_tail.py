#!/usr/bin/env python

# simple tail, doesnot need to read from stdin or handle errors
import sys

for curr_file in sys.argv[1:]:
    # print "==> {} <==".format(curr_file)
    with open(curr_file,'r') as f:
        for line in f.readlines()[-10:]:
            print line.strip('\n')
