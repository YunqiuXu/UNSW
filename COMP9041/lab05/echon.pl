#!/usr/bin/perl -w

# 2 arguments, if not 2 --> STDERR
# if the first arguments is not non-negative integer --> STDERR

# Check the number of argv
$num_argv = @ARGV;
if($num_argv != 2){
    print STDERR "Usage: ./echon.pl <number of lines> <string>\n";
    exit(1);
}

# Check whether the first argv is a non-negative integer
$repeat = $ARGV[0];
if($repeat =~ m/\D/){
    print STDERR "./echon.pl: argument 1 must be a non-negative integer\n";
    exit(1);
}
if($repeat < 0){
    print STDERR "./echon.pl: argument 1 must be a non-negative integer\n";
    exit(1);
}

# loop
$count = 0;
while($count < $repeat){
    print "$ARGV[1]\n";
    $count++;
}
