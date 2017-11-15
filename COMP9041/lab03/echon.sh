#!/bin/sh

# COMP9041 Lab02 Exercise2 Repeated Echo

if [ $# -ne 2 ] # check the number of variables
then
    echo "Usage: ./echon.sh <number of lines> <string>" 1>&2 # error 1>&2
    exit
fi

# check whether var1 is a non-negative number
# for non-digit --> bitcount is not itself
var1test=$(echo $1 | bc)
if [ "$var1test" != "$1" ] # if test "..." != "..."
then 
    echo "./echon.sh: argument 1 must be a non-negative integer" 1>&2
    exit
fi

if [ $1 -lt 0 ]
then
    echo "./echon.sh: argument 1 must be a non-negative integer" 1>&2
    exit
fi

start=0
while [ $start -lt $1 ]
do
    echo $2
    start=`expr $start + 1`
done
