#!/bin/sh

start=1
end=100
incr=1

case $# in
1) end=$1 ;;
2) start=$1 end=$2 ;;
3) start=$12 incr=$1 end=$3 ;;
esac
 

# start the loop
while test $start -le $end
do
    echo $start
    start=`expr $start + 1`
done


# others are omitted
