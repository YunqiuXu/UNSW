#!/bin/bash

my_array=()

echo ${my_array[@]}

a=1
b=2
c=3
d=4
e=5

my_array[$a]=$a
echo ${my_array[@]}
my_array[$b]=$b
echo ${my_array[@]}
my_array[$c]=$c
echo ${my_array[@]}
my_array[$d]=$d
echo ${my_array[@]}
my_array[$e]=$e
echo ${my_array[@]}

