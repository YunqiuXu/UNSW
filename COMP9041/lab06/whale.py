#!/usr/bin/env python

# reimplement whale.pl using python
import sys,re

whale_record = sys.stdin.readlines();
curr_whale = sys.argv[1]
pod_count = 0
individual_count = 0

for pod in whale_record:
    pattern = "^[0-9]+ +" + curr_whale + "$"
    # print "Current pattern : " + pattern
    
    if re.match(pattern, pod):
        
        pod_count += 1
        individual_ob = pod.split(" ")[0] # note that we can not use " +" in python
        individual_count += int(individual_ob)
    
print "{} observations: {} pods, {} individuals".format(curr_whale, pod_count, individual_count)
