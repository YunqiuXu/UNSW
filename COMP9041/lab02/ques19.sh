#!/bin/bash
while read -r line
do
        length=${#line}
        # echo "The length is $length"
        new_length=`expr $length / 2 \* 2`
        # echo "The new length is $new_length"
        if [ $length -eq $new_length ]
        then
                num_a=`expr $length / 2`
                echo $line | egrep "^A{$num_a}B{$num_a}$"
        fi
done

# one line
while read -r line; do length=${#line};new_length=`expr $length / 2 \* 2` ; if [ $length -eq $new_length ]; then num_a=`expr $length / 2` | echo $line | egrep "^A\{$num_a\}B\{$num_a\}$"; fi; done < input.txt
