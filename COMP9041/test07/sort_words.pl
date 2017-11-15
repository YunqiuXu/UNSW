#!/usr/bin/perl -w

# sort each line in alphabetic order
@inputs = ();
while ($line = <STDIN>){
    push @inputs, $line;
}

foreach $line(@inputs){
    chomp $line;
    @splitted = split(" +", $line);
    @sorted = sort(@splitted);
    print "@sorted\n";
}
