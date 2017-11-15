#!/bin/sh

# **************************** #
# [ How to use it ] ./shuffle_test.sh shuffle.pl
# **************************** #

# function check_shuffle()
# input: $1 = list_length, $2 = shuffle_time, $3 = maximum_repeat, $4 = shuffle.pl
# output: return 1 if test fail, otherwise return 0
check_shuffle(){
    list_length=$1
    shuffle_time=$2
    maximum_repeat=$3
    perl_file=$4
    
    # generate original file
    origin_file=`echo "shuffle_test_file_0.txt"`
    i=0;while [ $i -lt $list_length ]; do echo $i; i=`expr $i + 1`; done >> $origin_file 
    
    # generate shuffle files
    file_index=1
    while [ $file_index -le $shuffle_time ]
    do
        shuffle_file=`echo "shuffle_test_file_$file_index.txt"`
        cat $origin_file | perl -w $perl_file >> $shuffle_file
        # file_list[$file_index]=$shuffle_file
        file_index=`expr $file_index + 1`
    done
    
    # check whether there are repeat pairs
    # if file_index = 5, the file is ..0, ..1, ..2, ..3, ..4
    repeat_count=0
    index1=0
    while [ $index1 -lt $file_index ]
    do
        file1=`echo "shuffle_test_file_$index1.txt"`
        index2=`expr $index1 + 1`

        while [ $index2 -lt $file_index ]
        do
            file2=`echo "shuffle_test_file_$index2.txt"`
            
            # echo "Compare $file1 with $file2"
            
            cmp -s $file1 $file2 ; status="$?"
            if [ $status -eq 0 ]
            then 
                # echo "repeated!!"
                repeat_count=`expr $repeat_count + 1`
                if [ $repeat_count -ge $maximum_repeat ]
                then
                    # echo "Maximum repeat"
                    rm -rf shuffle_test_file_*.txt
                    return 1 # test fail
                fi
            fi
            
            index2=`expr $index2 + 1`
        done
        
        index1=`expr $index1 + 1`
    done
    
    # remove all temp file
    rm -rf shuffle_test_file_*.txt
    return 0
}

# For each test case, I generate a list with 10 elements and shuffle it for 50 times, if there are more than 3 repeated pairs among all 51 lists, the test is failed, otherwise passed
# There will be 15 test cases
case_index=0
test_count=15
pass_count=0
fail_count=0
perl_file=$1
while [ $case_index -lt $test_count ]
do
    echo "Test case $case_index"
    check_shuffle 10 50 3 $perl_file
    
    if [ $? -eq 0 ]
    then
        echo "Test case $case_index passed"
        pass_count=`expr $pass_count + 1`
    else
        echo "Test case $case_index failed"
        fail_count=`expr $fail_count + 1`
    fi
    
    case_index=`expr $case_index + 1`
    echo "-----"
done
echo "All $test_count test cases, $pass_count pass, $fail_count fail"
    
    
    
