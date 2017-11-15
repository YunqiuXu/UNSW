#!/usr/bin/perl -w
# [PASSED]


$prefix = $ARGV[0];
$url = "http://www.timetable.unsw.edu.au/current/" . $prefix . "KENS.html";
open DATA, "wget -q -O- $url |" or die;
while ($line = <DATA>){
    if ($line =~ m/$prefix[0-9]{4}<\/a>/){
        $line =~ s/^.*href="//g;
        $line =~ s/\.html.*$//g;
        print "$line";
    }
}
