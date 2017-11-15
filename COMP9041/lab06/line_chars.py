#!/usr/bin/python
# written by andrewt@cse.unsw.edu.au as a 2041 lecture example
# Simple example reading a line of input and examining characters

import sys

sys.stdout.write("Enter some input: ")
line = sys.stdin.readline()
if not line:
    sys.stdout.write("%s: could not read any characters\n" % sys.argv[0])
line = line.rstrip('\n')
n_chars = len(line)
print("That line contained %s characters" % n_chars)
if n_chars > 0:
    first_char =line[0]
    last_char = line[-1]
    print("The first character was '%s'" % first_char)
    print("The last character was '%s'" % last_char)
