#!/usr/bin/perl -w

%uniq_set = ();
@result = ();

foreach $curr(@ARGV){
    if (not exists($uniq_set{$curr})){
        $uniq_set{$curr} = 1;
        push @result, $curr;
    }
}

print "@result\n";
