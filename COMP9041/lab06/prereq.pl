#!/usr/bin/perl -w

# extract prerequisites from both undergre and postgre
$keyword = $ARGV[0];
$under_url = "http://www.handbook.unsw.edu.au/undergraduate/courses/current/$keyword.html";
$post_url = "http://www.handbook.unsw.edu.au/postgraduate/courses/current/$keyword.html";

open DATA, "wget -q -O- $under_url $post_url |" or die;
%pre = (); # Hash is better than array for that I chan check repeated courses
while ($line = <DATA>) {
    # check whether this line contains prereq
    if ( $line =~ m/Prerequisite/ ){
        
        # print "Before adjustment: $line\n";
        $line =~ s/strong.*?$//g;
        # print "After adjustment: $line\n";
        
        $head_index = 0;
        $line_length = length $line;
        while ($head_index <= $line_length - 8){
            $word = substr($line, $head_index, 8);
            if ($word =~ m/^[A-Z]{4}[0-9]{4}$/ and not exists($pre{$word})){
                # print "$word is a new course!\n";
                $pre{$word} = 1;                  
            }
            $head_index++;
        }
    }
}

# output the result
@courses = keys %pre;
@courses = sort(@courses);
foreach $course(@courses){
    print "$course\n";
}
