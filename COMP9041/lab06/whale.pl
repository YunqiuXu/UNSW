#!/usr/bin/perl -w

# reads whale observations in the above format until the end-of-input 
@whale_record = ();
while($pod = <STDIN>){
    push @whale_record, $pod;
}

# check the appearance of given species
$curr_whale = $ARGV[0];
$pod_count = 0;
$individual_count = 0;
foreach $pod(@whale_record){
    if ($pod =~ m/^[0-9]+ +$curr_whale$/) {
        $pod_count++;
        @splitted = split(" +", $pod); # split by one or more spaces
        $individual_ob = $splitted[0];
        $individual_count += $individual_ob;
    }
}

print "$curr_whale observations: $pod_count pods, $individual_count individuals\n";
