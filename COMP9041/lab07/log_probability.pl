#!/usr/bin/perl -w

# prints the frequency with each artist uses a word specified as argument

$pattern_word = $ARGV[0];
foreach $file (glob "lyrics/*.txt") {
    @result = get_counts($file, $pattern_word);
    # print "@result\n";
    $total_count = $result[0];
    $word_count = $result[1];
    $log_freq = log(($word_count + 1) / $total_count);
    $file =~ s/^.*?\///g;
    $file =~ s/\.txt//g;
    $file =~ s/_/ /g;
    printf "log((%d+1)/%6d) = %8.4f %s\n", $word_count, $total_count, $log_freq, $file;
}


# input: file, word_pattern
# output: result = (total_count, word_count)
sub get_counts{
    my $file = $_[0];
    my $pattern_word = $_[1];
    $pattern_word = lc($pattern_word);
    my $total_count = 0;
    my $word_count = 0;
    
    open(my $DATA, '<', $file) or die("Can not open file, $!\n");
    while (my $line = <$DATA>){
        $line =~ s/^[^A-Za-z]+//;
        my @splitted_line = split('[^A-Za-z]+', $line);
        my $length = @splitted_line;
        $total_count = $total_count + $length;
        foreach my $word (@splitted_line){
            $word = lc($word);
            if ($word =~ m/^\Q$pattern_word\E$/){ # \Q \E escape
                $word_count++;
            }
        }
    }
    my @result = ();
    push(@result, $total_count);
    push(@result, $word_count);
    return @result;
}
