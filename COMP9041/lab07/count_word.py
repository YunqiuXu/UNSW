#!/usr/bin/env python

# count words from stdin
# all non [a-zA-Z] separate words will be regarded as separaters
import sys
import re

pattern_word = sys.argv[1]
pattern_word = pattern_word.lower()
count = 0

for line in sys.stdin:
    pattern_head = re.compile("^[^A-Za-z]+")
    line = re.sub(pattern_head, '', line)
    pattern_split = re.compile("[^A-Za-z]+")
    splitted_line = re.split(pattern_split, line)
    for word in splitted_line[:-1]:
        word = word.lower()
        if re.match(re.compile("^" + pattern_word + "$"), word):
            count += 1

print "{} occurred {} times".format(pattern_word, count)
