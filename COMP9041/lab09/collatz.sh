#!/bin/bash

# https://en.wikipedia.org/wiki/Collatz_conjecture
# https://xkcd.com/710/

n=65535
while ((n != 1))
do
	if ((n % 2 == 0))
	then
		n=$((n / 2))
	else
		n=$((3 * n + 1))
	fi
	echo $n
done
