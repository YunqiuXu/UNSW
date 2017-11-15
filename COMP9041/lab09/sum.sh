#!/bin/bash

# sum the integers $start .. $finish

start=1
finish=100
sum=0

i=1
while ((i <= finish))
do
    sum=$((sum + i))
    i=$((i + 1))
done

echo Sum of the integers $start .. $finish = $sum
