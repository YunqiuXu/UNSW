#!/usr/bin/python3


###############################################################################
#                            COMP9041 TEST 00                                 #
#                     Author : Yunqiu Xu (z5096489)                           # 
# Main contents:                                                              #
#   print                                                                     #
#   basic assignment and computaiton                                          #
###############################################################################


print("Case 1")
print()
print("Case with \"(\" and \";\" ")
print("String with end", end = ' ~~~ ')
print("blahblahblah")
print("-----")

print("Case 2")
a = 2 + (3 % 4.0) / 5
print(a)
print("-----")

print("Case 3")
b = (3.5 * a + 1) / (2.0 - 1.0)
print(b)
print("-----")

print("Case 4")
c = (((1 + 2) / a) * b) + a
print(c)
print("-----")

print("Case 5")
d = -8 // 3
print(10 % d + c)
print("-----")

print("Case 6")
e = 5
e += a
f = 6.0
f *= b
print("e is %.2f and f is %.2f."%(e,f))
print("-----")

print("Case 7")
g = 12
g //= a + 1
print("g is %.2f."%g)
print("-----")

print("Case 8")
a = int(a)
print("Now a is %s"%a)
print("-----")


