#!/usr/bin/env python

# ignore case and white-space when comapring lines
import sys


distinct_count = int(sys.argv[1])
total_count = 0
distinct_dict = {}

while True:
    try:
        curr_line = raw_input()
        curr_line = curr_line.lower()
        curr_line = curr_line.strip()
        # 可以直接这么用: curr_line = ' '.join(curr_line.split())
        curr_line = ' '.join(filter(None,curr_line.split()))
        
        if curr_line:
            total_count += 1
            if curr_line not in distinct_dict:
                distinct_dict[curr_line] = 1
        # print "Now we have read {} lines, {} unique".format(total_count, len(distinct_dict))
        if len(distinct_dict) == distinct_count:
            break
    except:
        break


if len(distinct_dict) == distinct_count:
    print "{} distinct lines seen after {} lines read.".format(distinct_count, total_count)
else:
    print "End of input reached after {} lines read -  {} different lines not seen.".format(total_count, distinct_count)
