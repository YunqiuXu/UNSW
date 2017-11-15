#!/bin/bash

# Printall occurances of executable programs with the specified names in $PATH
# Note use of tr to produce a space-separated list of directories suitable for a for loop.

# Breaks if directories contain spaces

if test $# = 0
then
    echo "Usage $0: <program>" 1>&2
    exit 1
fi

for program in "$@"
do
    program_found=''
    for directory in `echo "$PATH" | tr ':' ' '`
    do
        f="$directory/$program"
        if test -x "$f"
        then
            ls -ld "$f"
            program_found=1
        fi
    done
    if test -z $program_found
    then
        echo "$program not found"
    fi
done
