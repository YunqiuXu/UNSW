#!/usr/bin/perl -w

while($line = <STDIN>){
	$line =~ tr/[aeiouAEIOU]//d;
	print STDOUT $line;
}

