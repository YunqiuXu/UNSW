#!/usr/bin/env python

# count words from stdin
# all non [a-zA-Z] separate words will be regarded as separaters
import sys
import re

count = 0
for line in sys.stdin:
    pattern_head = re.compile("^[^A-Za-z]+")
    line = re.sub(pattern_head, '', line)
    pattern_split = re.compile("[^A-Za-z]+")
    splitted_line = re.split(pattern_split, line)
    count += len(splitted_line) - 1 # remove "\n"

print "{} words".format(count)
