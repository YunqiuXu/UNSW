#!/usr/bin/env python

import sys

# no argv
if len(sys.argv) == 1:
    print 
else:
    dict_ = {}
    uniq_list = [] # keep order, 其实可以直接用这个检查, 只是复杂度差点儿
    for item in sys.argv[1:]:
        # print item
        if item not in dict_:
            dict_[item] = 1
            uniq_list.append(item)
    print ' '.join(uniq_list)
