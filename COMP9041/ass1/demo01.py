#!/usr/bin/python3


###############################################################################
#                            COMP9041 DEMO 01                                 #
#                     Author : Yunqiu Xu (z5096489)                           # 
#                                                                             #
# Bubble Sort                                                                 #
# python3 demo01 10 25 1 56 74 69 --> 1 10 25 56 69 74                        #
###############################################################################


import sys

nums = []
for num in sys.argv[1:]:
    nums.append(num)

for index in range(len(nums)):
    for i in range(1,len(nums)-index):
        if nums[i-1] > nums[i]:
            temp = nums[i-1]
            nums[i-1] = nums[i]
            nums[i] = temp

result = ' '.join(nums)
print(result)
