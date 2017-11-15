#!/usr/bin/perl -w

%inputs = ();
$repeat_time = $ARGV[0];
while($curr_line = <STDIN>){
    if(exists $inputs{$curr_line}){
        $inputs{$curr_line}++;
    }
    else{
        $inputs{$curr_line} = 1;
    }
    if($inputs{$curr_line} == $repeat_time){
        print "Snap: $curr_line";
        exit(0);
    }
}
