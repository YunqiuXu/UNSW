#!/usr/bin/python3


###############################################################################
#                            COMP9041 DEMO 03                                 #
#                     Author : Yunqiu Xu (z5096489)                           # 
#                                                                             #
# Merge 2 sorted lists                                                        #
###############################################################################


list_a = [2,4,6,8,9,10]
list_b = [0,1,3,6,7,9,100,134]
count_a = 0
count_b = 0

result = []
for i in range(count_a,len(list_a)):
    for j in range(count_b,len(list_b)):
        if list_b[j] <= list_a[i] :
            result.append(list_b[j])
            count_b += 1
        else:
            result.append(list_a[i])
            count_a += 1
            break


if count_a < len(list_a) :
    for i in range(count_a,len(list_a)):
        result.append(list_a[i])
if count_b < len(list_b) :
    for j in range(count_b,len(list_b)):
        result.append(list_b[j])

for i in result:
    print(i)


