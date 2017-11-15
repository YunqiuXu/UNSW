#!/usr/bin/python3


###############################################################################
#                            COMP9041 DEMO 02                                 #
#                     Author : Yunqiu Xu (z5096489)                           # 
#                                                                             #
# Devowel: delete all vowels                                                  #
###############################################################################


import fileinput, re

for line in fileinput.input():
    line = re.sub(r'[AEIOUaeiou]', '', line)
    print(line, end='')
