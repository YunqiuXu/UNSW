#!/bin/sh

for file in `find $1 -type f`
do 
    tr "2041" "2042" < $file
    tr "9041" "9042" < $file
done
