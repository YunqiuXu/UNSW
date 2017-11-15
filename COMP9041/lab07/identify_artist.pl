#!/usr/bin/perl -w

# input : 1 or more files
# output: "$file most resembles the work of $Author (log-probability=___)"
# '-d' flag --> display all log_probabilities
# use a hash table of hash tables indexed by artist and word to store the word counts

# Steps:
# 1. For each artest, get word count
# 2. For each file, split it with pattern words
# 3. For each pattern word and artist, calsulate its log prob --> return a hash value $hash{$artist}{$word} = $log
# 4. sum log for the one artist
# 5. find the largest one 

if ($ARGV[0] =~ m/^-d$/){ # display mode
    $start_position = 1;
}
else{
    $start_position = 0;
}

$song_file_len = @ARGV;

# get total count of each artist
%artist_total_count = get_artist_total_count();
@artists = keys %artist_total_count;

foreach $song_file (@ARGV[$start_position..$song_file_len-1]){

    # get all pattern words for this file: $pattern_words{$pattern_word} = $repeat_time
    %pattern_words = get_pattern_words($song_file); 
    @pattern_words_keys = keys %pattern_words;

    # init final result for this file :  $log_prob_all{$artist} = $log_prob_all
    %log_prob_all = ();

    # for each artist, get count of each pattern word
    foreach $artist(@artists){

        # generate another hash array to store word count
        %pattern_words_count = ();
        foreach $pattern_word (@pattern_words_keys){
            $pattern_words_count{$pattern_word} = 0;
        }

        $log_prob_all{$artist} = 0;
        open($DATA, '<', $artist) or die("Can not open file, $!\n");
        while ($line = <$DATA>){
            $line =~ s/^[^A-Za-z]+//;
            @splitted_line = split('[^A-Za-z]+', $line);
            foreach $word (@splitted_line){
                $word = lc($word);
                if (exists($pattern_words_count{$word})){
                    $pattern_words_count{$word}++;
                }
            }
        }
        # get the sum of log_prob
        $total_count = $artist_total_count{$artist};
        foreach $pattern_word (@pattern_words_keys){
            $repeat_time = $pattern_words{$pattern_word};
            $word_count = $pattern_words_count{$pattern_word};
            $log_probs = log(($word_count + 1) / $total_count);
            $log_prob_all{$artist} = $log_prob_all{$artist} + $log_probs * $repeat_time;
        }
    }

    # %log_prob_all{$artist} = $log_sum
    # now we get the sum of log_probs for each artist
    # then we print them and get the one with largest prob
    @sorted_artists = sort{ $log_prob_all{$b} <=> $log_prob_all{$a} } keys(%log_prob_all);
    $max_artist = $sorted_artists[0];
    $max_log = $log_prob_all{$max_artist};
    $max_artist =~ s/^.*?\///g;
    $max_artist =~ s/\.txt//g;
    $max_artist =~ s/_/ /g;

    if ($start_position == 1){
        foreach $artist(@sorted_artists){
            $curr_log = $log_prob_all{$artist};
            $artist =~ s/^.*?\///g;
            $artist =~ s/\.txt//g;
            $artist =~ s/_/ /g;
            printf "%s: log_probability of %.1f for %s\n", $song_file, $curr_log, $artist;
        }
    }
    
    # print the largest one
    printf "%s most resembles the work of %s (log-probability=%.1f)\n", $song_file, $max_artist, $max_log;
}




############################# FUNCTION PASSED #######################
# get_artist_total_count
# Input: none
# Output: hash array {artist : word_count} 
sub get_artist_total_count{
    my %result = ();
    foreach my $file (glob "lyrics/*.txt") {
        $total_count = 0;
        open(my $DATA, '<', $file) or die("Can not open file, $!\n");
        while (my $line = <$DATA>){
            $line =~ s/^[^A-Za-z]+//;
            my @splitted_line = split('[^A-Za-z]+', $line);
            my $length = @splitted_line;
            $total_count = $total_count + $length;
        }
        $result{$file} = $total_count; 
    }
    return %result;
}
#####################################################################

############################# FUNCTION PASSED #######################
# get pattern words
# input: file_name(template song)
# output: an hash array of pattern words(lowercase,key), and their count(value)
sub get_pattern_words{
    my $file = $_[0];
    my %pattern_words = ();
    open(my $DATA, '<', $file) or die("Can not open file, $!\n");
    while (my $line = <$DATA>){
        $line =~ s/^[^A-Za-z]+//;
        my @splitted_line = split('[^A-Za-z]+', $line);
        foreach my $word (@splitted_line){
            $word = lc($word);
            if (exists($pattern_words{$word})){
                $pattern_words{$word}++;
            }
            else{
                $pattern_words{$word} = 1;
            }
        }
    }
    return %pattern_words;
}
#####################################################################
