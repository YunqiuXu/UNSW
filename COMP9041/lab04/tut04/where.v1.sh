#!/bin/bash


# won't work if dir contain spaces, instead of break down

if test $# = 0
then
    echo "Usage $0: <program>" 1>&2
    exit 1
fi

for program in "$@"
do
    echo "$PATH"|
    tr ':' '\n'|
    while read directory
    do
        f="$directory/$program"
        if test -x "$f"
        then
            ls -ld "$f"
        fi
    done|
    egrep '.' || echo "$program not found"
done
