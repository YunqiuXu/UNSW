#!/bin/sh

# check a large number of C programs for missing include files
# for *.c, we may find include ..., then we check whether all files in "include" line are exist

for c_file in "$@"
do
    cat "$c_file" | egrep "^#include \"" | cut -d'"' -f2 | while read h_file
    do
        if test -f "$h_file"
        then
            continue
        else
            echo "$h_file included into $c_file does not exist"
        fi
    done
done

