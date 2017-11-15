#!/usr/bin/env python

import sys

lines = []
for curr_line in sys.stdin.readlines():
    # 不需要这么麻烦, 直接split()就好, 默认空格都削去
    curr_line = ' '.join(sorted(filter(None, curr_line.split())))
    lines.append(curr_line)
    
for curr_line in lines:
    print curr_line


