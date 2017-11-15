#!/usr/bin/env python

import sys
import re
import glob

def get_counts(file, pattern_word):
    pattern_word = pattern_word.lower()
    total_count = 0
    word_count = 0

    with open(file, 'r') as f:
        for line in f.readlines():
            pattern_head = re.compile("^[^A-Za-z]+")
            line = re.sub(pattern_head, '', line)
            pattern_split = re.compile("[^A-Za-z]+")
            splitted_line = re.split(pattern_split, line)
            total_count += len(splitted_line) - 1
            for word in splitted_line[:-1]:
                word = word.lower()
                if re.match(re.compile("^" + pattern_word + "$"), word):
                    word_count += 1

    return total_count, word_count

pattern_word = sys.argv[1]

for file in sorted(glob.glob("lyrics/*.txt")):
    total_count, word_count = get_counts(file, pattern_word)
    freq = word_count * 1.0 / total_count
    pat1 = re.compile("^.*?\/")
    file = re.sub(pat1, '', file)
    pat2 = re.compile("\.txt")
    file = re.sub(pat2, '', file)
    pat3 = re.compile("_")
    file = re.sub(pat3, ' ', file)
    print "{:4d}/{:6d} = {:.9f} {}".format(word_count, total_count, freq, file)



