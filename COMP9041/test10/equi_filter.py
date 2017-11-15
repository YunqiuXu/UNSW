#!/usr/bin/env python

import sys

def check_equal(word):
    word = word.lower()
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    counts = letter_count.values()
    for curr_count in counts:
        if curr_count != counts[0]:
            return 0
    return 1


for line in sys.stdin.readlines():
    words = line.split()
    result = []
    for word in words:
        if check_equal(word) == 1:
            result.append(word)
    print " ".join(result)

