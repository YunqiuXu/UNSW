#!/usr/bin/python3


###############################################################################
#                            COMP9041 DEMO 00                                 #
#                     Author : Yunqiu Xu (z5096489)                           # 
#                                                                             #
# Find greatest common divisor of 2 numbers                                   #
###############################################################################


import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())

if num1 > num2:
    smaller = num2
else:
    smaller = num1

for i in range(1, smaller + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD of %d and %d is %d"%(num1, num2, gcd))
