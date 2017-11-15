#!/usr/bin/env python

# implement mapping digits with python
import sys,re
result = []
for line in sys.stdin.readlines():
    pattern1 = "[0-4]"
    pattern2 = "[6-9]"
    line=line.strip('\n')
    line = re.sub(pattern1, "<", line)
    line = re.sub(pattern2, ">", line)
    result.append(line)

for line in result:
    print line
