#!/usr/bin/env python

# reimplement all_wales using python
import sys, re
whale_record = sys.stdin.readlines();

# scan each line
whales_namelist = []
whales_odd = {}
whales_ind = {}
for pod in whale_record:

    # split the pod by number and strings
    pod = pod.strip() # remove the spaces
    splitted = pod.split(" ") # note that we can not use " +"
    splitted = filter(None, splitted) # remove those ""
    
    individual_ob = int(splitted[0])
    whale_name = ' '.join(splitted[1:])
    whale_name = whale_name.lower() # all lower case
    whale_name = whale_name.strip('\n') # remove \n
    if whale_name[-1] == 's':
        whale_name = whale_name[:-1] # remove s at last
    
    # check whether this whale has been observed
    if whale_name in whales_odd:
        whales_odd[whale_name] += 1
        whales_ind[whale_name] += individual_ob
    else: # new whale
        whales_namelist.append(whale_name)
        whales_odd[whale_name] = 1
        whales_ind[whale_name] = individual_ob

# output the data in alphabetical order
whales_namelist = sorted(whales_namelist)
for whale_name in whales_namelist:
    print "{} observations: {} pods, {} individuals".format(whale_name, whales_odd[whale_name], whales_ind[whale_name])


