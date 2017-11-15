#!/usr/bin/perl -w

# ./xxx n
# read inputs until n distinct are finded
# ignore case and white-space when comapring lines.

%distinct = ();
$all_count = 0;
$curr_distinct = 0;
$total_dictinct = $ARGV[0];

while($line = <STDIN>){
    $all_count++;
    chomp $line;
    $line =~ s/^\s+//g;
    $line =~ s/\s+$//g;
    $line =~ s/\s+/ /g;
    $line = lc($line);
    if (not exists ($distinct{$line})){
        $distinct{$line} = 1;
        $curr_distinct++;
        if ($curr_distinct == $total_dictinct){
            print "$total_dictinct distinct lines seen after $all_count lines read.\n";
            exit 0;
        }
    }
}
print "End of input reached after $all_count lines read - $total_dictinct different lines not seen.\n"
