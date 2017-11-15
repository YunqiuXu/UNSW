#!/bin/bash

max=42
a=1 
while ((a < max))
do
	b=$a 
	while ((b < max))
	do
		c=$b 
		while ((c < max))
		do
			if ((a * a + b * b == c * c))
			then
			    echo $a $b $c is a Pythagorean Triple
			fi
			c=$((c + 1))
		done
		b=$((b + 1))
	done
	a=$((a + 1))
done
