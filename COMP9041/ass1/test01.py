#!/usr/bin/python3


###############################################################################
#                            COMP9041 TEST 01                                 #
#                     Author : Yunqiu Xu (z5096489)                           # 
# Main contents:                                                              #
#   bit manipulation                                                          #
#   logical comparasion                                                       #
#   if - elif - else statement                                                #
###############################################################################


print("Case 1")
if (2 ^ 0 > 0) < 2 : print("Yes")
print("-----")

print("Case 2")
if 10 & 10 != 0: 
    print("Yes")
print("-----")

print("Case 3")
a = 1
b = 2
if a | b > 0: print("Yes")
print("-----")

print("Case 4")
a = 2
b = 4
if (a ^ b != 4) != 2: 
    print("Yes")
print("-----")

print("Case 5")
a = 1
b = 2
c = 1
d = 4
e = 1
if a << b <= c << (d >> e): print("Yes")
print("-----")

print("Case 6")
a = 4
if ~-a > 0: 
    print("Yes")
print("-----")

print("Case 7")
a = 1
b = 2
c = 0
d = 0
if a + b >= c + d: print("Yes")
print("-----")

print("Case 8")
c = 5
d = 4
if c >= 5 and d >= 4: 
    print("Yes")
print("-----")

print("Case 9")
a = 1
b = 6
andy = 30
notnot = -1
if (a + b > 5) and ((andy / 6 != 6) or not notnot): print("Yes")
print("-----")


