#!/bin/sh

for file in $@
do 
    tr "2041" "2042" < $file
    tr "9041" "9042" < $file
done
