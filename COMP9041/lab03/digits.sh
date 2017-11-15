#!/bin/sh

# COMP9041 Lab02 Exercise1 Mapping Digits

while read line
do
    echo $line | tr '0-4' '<' | tr '6-9' '>'
done
