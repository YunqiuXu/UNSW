#!/bin/sh

# rename all files in subdirestories
# sh tut04q3.sh Test

# step 1 : rename all directories
for filepath in `find $1 -type d`
do
    echo "$filepath"
    newpath=`echo $filepath | tr "2041" "2042" | tr "9041" "9042"`
    echo "$newpath"
    if [ "$filepath" != "$newpath" ]
    then
        echo "change!"
        mv $filepath $newpath
    fi
done

# step 2 : rename all files
for filepath in `find $1 -type f`
do
    echo "$filepath"
    newpath=`echo $filepath | tr "2041" "2042" | tr "9041" "9042"`
    echo "$newpath"
    if [ "$filepath" != "$newpath" ]
    then
        echo "change!"
        mv $filepath $newpath
    fi
done



