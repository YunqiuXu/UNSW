#!/bin/sh

# change all files with "[29]041" as "[29]042"
for filename in `ls *[29]041*`
do
    newname=`echo $filename | tr "2041" "2042" | tr "9041" "9042"`
    mv $filename $newname
done
