#!/usr/bin/perl -w

# count words from stdin
# all non [a-zA-Z] separate words will be regarded as separaters
$count = 0;
while ($line = <STDIN>){
    # remove all non-word chars at head, otherwise the length will be one more
    $line =~ s/^[^A-Za-z]+//;
    @splitted_line = split('[^A-Za-z]+', $line);
    $length = @splitted_line;
    $count = $count + $length;
}
print "$count words\n";
