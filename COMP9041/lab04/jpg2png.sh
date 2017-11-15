#!/bin/sh

# Exercise 1: convert jpg to png
# Your script should stop with an appropriate error message and exit status if the PNG file already exists
ls *.jpg | while read jpg_file
do    
    # check whether the png file exists
    new_name=`echo "$jpg_file" | sed 's/jpg/png/g'`
    if test -f "$new_name"
    then 
        echo "$new_name already exists" 1>&2
        exit 1
    else
        convert "$jpg_file" "$new_name"
        rm -rf "$jpg_file"
    fi
done
