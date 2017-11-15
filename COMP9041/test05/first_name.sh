#!/bin/sh

# get the first name for [29]041 then compute the most common one

egrep "COMP[29]041" $1 | cut -d'|' -f3 | cut -d' ' -f2 | sort | uniq -c | sort -rn | head -1 | sed "s/^.*[0-9] //g"

