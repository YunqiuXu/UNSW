#!/bin/sh

# COMP9041 Lab02 Exercise3 : File Sizes

small=()
medium=()
large=()

file_number=`ls -l | wc -l`
file_number=`expr $file_number - 1`
file_count=0 

wc -l `ls *` | while read line
do
        size=`echo $line | cut -d' ' -f1`
        file_name=`echo $line | cut -d' ' -f2`

        if [ $size -lt 10 ]
        then
            small[${#small[@]}]=$file_name
        elif [ $size -lt 100 ]
        then 
            medium[${#medium[@]}]=$file_name
        else
            large[${#large[@]}]=$file_name
        fi

        file_count=`expr $file_count + 1`

        if [ "$file_count" -ge "$file_number" ]
        then
            echo "Small files: ${small[@]}"
            echo "Medium-sized files: ${medium[@]}"
            echo "Large files: ${large[@]}" 
            exit
        fi
done


