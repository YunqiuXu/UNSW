#!/bin/bash

# calculate powers of 2 by repeated addition

i=1
j=1
while ((i < 31))
do
    j=$((j + j))
    i=$((i + 1))
    echo $i $j
done
