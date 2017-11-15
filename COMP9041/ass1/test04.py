#!/usr/bin/python3


###############################################################################
#                            COMP9041 TEST 04                                 #
#                     Author : Yunqiu Xu (z5096489)                           # 
# Main contents:                                                              #
#   some topics for subset5                                                   #
###############################################################################


import sys, re, fileinput

print("Case 1")
first_argv = sys.argv[1]
print("First argument : %s"%first_argv)
last_argv = sys.argv[-1]
print("Last argument : %s"%last_argv)
print("-----")

print("Case 2")
for i in range(1,len(sys.argv)):
    print(sys.argv[i])
print("-----")

print("Case 3")
for arg in sys.argv[1:]:
    print(arg)
print("-----")

print("Case 4")
line = "I1will2always,be,with!!!you"
line = re.sub(r'[0-9,!]+', ' ', line)
print(line)
print("-----")

print("Case 5")
print(' '.join(sys.argv[1:]))
print("-----")

print("Case 6")
dic1 = {}
dic2 = {"A":1, "B":2}
if "A" in dic1:
    print("Dic1")
elif "A" in dic2:
    print("Dic2")
else:
    print("Nothing")
