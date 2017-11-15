#!/usr/bin/env python
import sys
import re
import glob
import math


############################# FUNCTION PASSED #######################
# get_artist_total_count
# Input: none
# Output: dict {artist : word_count} 
def get_artist_total_count():
    result = {}
    sorted_files = sorted(glob.glob("lyrics/*.txt"))
    for file in sorted_files:
        total_count = 0
        with open(file,'r') as f:
            for line in f.readlines():
                pattern_head = re.compile("^[^A-Za-z]+")
                line = re.sub(pattern_head, '', line)
                pattern_split = re.compile("[^A-Za-z]+")
                splitted_line = re.split(pattern_split, line)
                total_count += len(splitted_line) - 1
        result[file] = total_count
    return result
#####################################################################

############################# FUNCTION PASSED #######################
# get pattern words
# input: file_name(template song)
# output: a dict of pattern words(lowercase,key), and their count(value)
def get_pattern_words(file):
    pattern_words = {}
    with open(file,'r') as f:
        for line in f.readlines():
            pattern_head = re.compile("^[^A-Za-z]+")
            line = re.sub(pattern_head, '', line)
            pattern_split = re.compile("[^A-Za-z]+")
            splitted_line = re.split(pattern_split, line)
            for word in splitted_line[:-1]:
                word = word.lower()
                if word in pattern_words:
                    pattern_words[word] += 1
                else:
                    pattern_words[word] = 1
    return pattern_words
#####################################################################

# main_part
if sys.argv[1] == '-d':
    start_position = 2
else:
    start_position = 1

# get total count of each artist
artist_total_count = get_artist_total_count()
artists = artist_total_count.keys()

for song_file in sys.argv[start_position:]:
    pattern_words = get_pattern_words(song_file)
    pattern_words_keys = pattern_words.keys()

    # init final result for this file :  $log_prob_all{$artist} = $log_prob_all
    log_prob_all = {}

    # for each artist, get count of each pattern word
    for artist in artists:

        # generate another hash array to store word count
        pattern_words_count = {}
        for pattern_word in pattern_words_keys:
            pattern_words_count[pattern_word] = 0

        log_prob_all[artist] = 0
        with open(artist,'r') as f:
            for line in f.readlines():
                pattern_head = re.compile("^[^A-Za-z]+")
                line = re.sub(pattern_head, '', line)
                pattern_split = re.compile("[^A-Za-z]+")
                splitted_line = re.split(pattern_split, line)
                for word in splitted_line[:-1]:
                    word = word.lower()
                    if word in pattern_words_count:
                        pattern_words_count[word] += 1

        # get the sum of log_prob
        total_count = artist_total_count[artist]
        for pattern_word in pattern_words_keys:
            repeat_time = pattern_words[pattern_word]
            word_count = pattern_words_count[pattern_word]
            log_freq = math.log((word_count * 1.0 + 1) / total_count)
            log_prob_all[artist] += log_freq * repeat_time

    # %log_prob_all{$artist} = $log_sum
    # now we get the sum of log_probs for each artist
    # then we print them and get the one with largest prob

    # sort the dict by value in reverse
    sorted_artists = sorted(log_prob_all.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    max_artist = sorted_artists[0][0]
    max_log = sorted_artists[0][1]
    pat1 = re.compile("^.*?\/")
    max_artist = re.sub(pat1, '', max_artist)
    pat2 = re.compile("\.txt")
    max_artist = re.sub(pat2, '', max_artist)
    pat3 = re.compile("_")
    max_artist = re.sub(pat3, ' ', max_artist)

    if start_position == 2:
        for pair in sorted_artists:
            artist = pair[0]
            curr_log = pair[1]
            pat1 = re.compile("^.*?\/")
            artist = re.sub(pat1, '', artist)
            pat2 = re.compile("\.txt")
            artist = re.sub(pat2, '', artist)
            pat3 = re.compile("_")
            artist = re.sub(pat3, ' ', artist)
            print "{}: log_probability of {:.1f} for {}".format(song_file, curr_log, artist)

    print "{} most resembles the work of {} (log-probability={:.1f})".format(song_file, max_artist, max_log)


