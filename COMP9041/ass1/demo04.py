#!/usr/bin/python3


###############################################################################
#                            COMP9041 DEMO 04                                 #
#                     Author : Yunqiu Xu (z5096489)                           # 
#                                                                             #
# Find single number : given a list, all numbers occur 3 times except one,    #
# find this single one.                                                       #
# []                                                                          #
###############################################################################


import sys

my_list = [3,1,5,4,3,2,3,5,2,4,5,4,2]
ones = 0
twos = 0
for ele in my_list: 
    ones = ones^ele & ~twos 
    twos = twos^ele & ~ones


sys.stdout.write("Now print the result:")
print(ones)
