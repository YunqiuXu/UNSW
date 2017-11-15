#!/usr/bin/perl -w

@arr = ();
while ($line = <STDIN>){
    push(@arr, $line);
}

foreach $line(@arr){
    $line =~ s/[0-9]+//g;
    print "$line";
}

    
