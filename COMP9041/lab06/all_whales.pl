#!/usr/bin/perl -w

# count all whale observations
# I use 2 hash list to represent the whale_name-pod-ind pair
# key: whale_name

# reads whale observations in the above format until the end-of-input 
@whale_record = ();
while($pod = <STDIN>){
    push @whale_record, $pod;
}

# scan each line
@whales_namelist = ();
%whales_odd = ();
%whales_ind = ();
foreach $pod(@whale_record){
    # split the pod by number and strings
    $pod =~ s/^\s+|\s+$//g; # remove the spaces
    @splitted = split(" +", $pod);
    $splitted_length = @splitted;
    
    $individual_ob = $splitted[0];
    $whale_name = join(' ', @splitted[1..$splitted_length-1]); # join the rest elements as whale name, or [1..$#splitted]
    $whale_name = lc($whale_name); # all lower case
    $whale_name =~ s/s$//; # remove s at last  
    chomp $whale_name; # remove \n
    
    # test: passed
    # print "whale name is $whale_name";
    # print "the observations in this pod is $individual_ob\n";
    
    # check whether this whale has been observed
    if (exists($whales_odd{$whale_name})){
        # print "Has been observed before\n";
        $whales_odd{$whale_name}++;
        $whales_ind{$whale_name} += $individual_ob;
    }
    else{ # new whale
        # print "Has not been observed before\n";
        push @whales_namelist, $whale_name;
        $whales_odd{$whale_name} = 1;
        $whales_ind{$whale_name} = $individual_ob;
    }
}

# output the data in alphabetical order
@whales_namelist = sort(@whales_namelist);
foreach $whale_name(@whales_namelist){
    print "$whale_name observations: $whales_odd{$whale_name} pods, $whales_ind{$whale_name} individuals\n";
}

