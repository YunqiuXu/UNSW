#!/bin/sh

# changes the name of all files with the suffix .htm in the current directory to have the suffix .html
# stop with EXACTLY the error message shown below and exit status 1 if the .html file already exists

ls | egrep "\.htm$" | while read old_name
do
    new_name=`echo "$old_name" | sed "s/\.htm$/.html/g"`  
    if test -f "$new_name"
    then
        echo "$new_name exists" 1>&2
        exit 1
    else 
        mv "$old_name" "$new_name"
    fi
done
