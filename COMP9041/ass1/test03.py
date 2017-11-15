#!/usr/bin/python3


###############################################################################
#                            COMP9041 TEST 03                                 #
#                     Author : Yunqiu Xu (z5096489)                           # 
# Main contents:                                                              #
#   more list manipulations                                                   #
###############################################################################


print("Case 1")
my_list = []
print(len(my_list))
my_list.append(int(1.5))
print(len(my_list))
print(my_list[0])
print("-----")

print("Case 2")
a = 1
b = 2
my_list = [a , b, "Hello", 0.1]
for i in my_list: print(i, end = ' ')
print()
print("-----")

print("Case 3")
for i in range(5): print("Current line is \"%s\""%i)
print("-----")

print("Case 4")
my_list = ["I","love","Python","and","Perl"]
print(my_list[0])
x = my_list[4]
print(x)
print(my_list[-1])
print("-----")

print("Case 5")
my_list1 = [1,2]
my_list2 = [6,-7,8]
my_list3 = [1.5,-1.5]
result = (my_list1[1] + my_list2[-1]) / my_list3[1] + my_list2[2]
print(result)
print("-----")

print("Case 6")
my_list = [1,2,3]
my_list.pop()
for i in my_list: print(i, end = ' ')
print()
print("-----")

print("Case 7")
my_list = [1,2,3]
my_list.append(4)
my_list.append(5)
for i in my_list: print(i, end = ' ')
print()
print("-----")

print("Case 8")
my_list = [1,2,3]
x = my_list.pop(2)
print(x + my_list.pop(0) * 2)
for i in my_list: print(i, end = ' ')
print()
print("-----")

print("Case 9")
my_list = [1,2,3,4,5]
x = (len(my_list) + 3) / 1.4
print(x)
y = int(x)
for i in range(y) : print(i, end = ' ')
print()
print("-----")

print("Case 10")
my_list = [3,1,8,2,5,4]
x = sorted(my_list)
for i in x: 
    print(i)
for i in sorted(my_list):
    print(i)
print("-----")

print("Case 11")
my_list = ["To", "be", "or", "not", "to", "be"]
x = my_list[1:3]
for i in x: print(i, end = ' ')
x = my_list[1:]
for i in x: print(i, end = ' ')
x = my_list[:3]
for i in x: print(i, end = ' ')
x = my_list[-6:-1]
for i in x: print(i, end = ' ')
x = my_list[-1:]
for i in x: print(i, end = ' ')
x = my_list[:-1]
for i in x: print(i, end = ' ')
a = 2
b = 4
for i in my_list[a:b]: print(i, end = ' ')
for i in my_list[2:-1]: print(i, end = ' ')
print()
print("-----")

print("Case 12")
my_list = [2,1,3,6,5,4]
i = 0
while i < len(my_list):
    if my_list[i] == i + 1:
        print("True")
    else:
        print("False")
    i += 1
print("-----")

print("Case 13")
my_list = [0]
for i in range(1, 5):
    my_list.append(my_list[i // 2] + i % 2)
for i in my_list: print(i, end = ' ')
print()
print("-----")

print("Case 14")
my_list = [1,2,3]
my_list[2] = 1
my_list[0] = 3
for i in my_list: print(i, end = ' ')
print()
print("-----")






