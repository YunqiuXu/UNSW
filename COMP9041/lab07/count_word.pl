#!/usr/bin/perl -w

# count word from stdin
# need to transform each word into lower case


$pattern_word = $ARGV[0];
$pattern_word = lc($pattern_word);
$count = 0;
while ($line = <STDIN>){
    $line =~ s/^[^A-Za-z]+//;
    @splitted_line = split('[^A-Za-z]+', $line);
    # foreach $word ($line =~ m/[a-z]+/g) ...
    foreach $word (@splitted_line){
        $word = lc($word);
        if ($word =~ m/^\Q$pattern_word\E$/){ # \Q \E escape
            $count++;
        }
    }
}
print "$pattern_word occurred $count times\n"; 
