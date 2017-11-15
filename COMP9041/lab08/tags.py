#!/usr/bin/env python

# [NOT PASSED CURRENTLY]


# given the URL of a web page fetches it by running wget and prints the HTML tags it uses
# all tags are in lower case, sorted by key
# avoid the content within HTML comments
# -f option:  to tags.py which indicates the tags are to printed in increasing order of frequency --> sorted by value

# some cases : 
# <div class = ...> remove all behind space
# </div> --> NO

import re, sys
from urllib import urlopen
import bs4 as BeautifulSoup

# get the content
if sys.argv[1] == "-f":
    url = sys.argv[2]
else:
    url = sys.argv[1]
response = urlopen(url)
webpage = response.read()
soup = BeautifulSoup.BeautifulSoup(webpage, "lxml")

#print webpage
#exit()

# get all tags
tags = [tag.name for tag in soup.find_all()]
tag_dict = {}
for tag in tags:
    if tag in tag_dict:
        tag_dict[tag] += 1
    else:
        tag_dict[tag] = 1

# Sort and output
if sys.argv[1] == "-f": # sort by value, if value is same --> sort by key
    sorted_tag_dict = sorted(tag_dict.items(), key=lambda x:x[1])
    i = 0
    while i < len(sorted_tag_dict):
        curr_count = sorted_tag_dict[i][1]
        bag = {}
        while sorted_tag_dict[i][1] == curr_count:
            bag[sorted_tag_dict[i][0]] = sorted_tag_dict[i][1]
            i += 1
            if i >= len(sorted_tag_dict):
                break
        bag_keys = bag.keys()
        for bag_key in sorted(bag_keys):
            print "{} {}".format(bag_key, bag[bag_key])



else: # sort by key
    tag_keys = tag_dict.keys()
    for tag_key in sorted(tag_keys):
        print "{} {}".format(tag_key, tag_dict[tag_key])

