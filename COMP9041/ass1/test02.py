#!/usr/bin/python3


###############################################################################
#                            COMP9041 TEST 02                                 #
#                     Author : Yunqiu Xu (z5096489)                           # 
# Main contents:                                                              #
#   loop                                                                      #
#   break and continue                                                        #
#   sys methods                                                               #
#   if - elif - else statement                                                #
#   list manipulation                                                         #
###############################################################################


import sys

print("Case 1")
x = 1
while x <= 10: print(x); x = x + 1
while x <= 10:
    print(x)
    x += 1
print("-----")

print("Case 2")
x = 1
while x < 10:
    y = 1
    while y <= x:
        sys.stdout.write("*")
        y = y + 1
    print()
    x = x + 1
print("-----")

print("Case 3")
count = 0
i = 2
while i < 100:
    k = i/2
    j = 2
    while j <= k:
        k = i % j
        if k == 0:
            count = count - 1
            break
        k = i/2
        j = j + 1
    count = count + 1
    i = i + 1
print(count)
print("-----")

print("Case 4")
for x in range(10): print(x)
for x in range(3):
    for y in range(2):
        print("X is %d and Y is %d"%(x,y))
print("-----")

print("Case 5")
for x in range(10):
    if x % 2 == 0:
        print("Continue")
        continue
    if x == 7:
        print("Break")
        break
    print("Other cases: x = %d"%x)
print("-----")

print("Case 6")
count = 0
for i in range(2, 100):
    k = i // 2
    j = 2
    for j in range(2, k + 1):
        k = i % j
        if k == 0:
            count = count - 1
            break
        k = i // 2
    count = count + 1
print(count)
print("-----")

print("Case 7")
std1 = sys.stdin.readlines()
for i in std1:
    print("Line %s"%i)
print("-----")

print("Case 8")
for i in sys.stdin.readlines():
    print("Line %s"%i)
print("-----")

print("Case 9")
for i in sys.stdin.readlines(): print("Line %s"%i)
print("-----")

print("Case 10")
for i in range(3):
    print("Enter: ")
    curr = sys.stdin.readline()
    print("Current input : %s"%curr)
print("-----")

