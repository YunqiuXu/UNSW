#!/usr/bin/perl -w

# read lines from standardinput until end-of-input
# print the lines with largest number
# numbers do not contain white space, commas or other extra characters
# Lines may contain multiple numbers and they may contain any number of any character between the numbers.
# If the largest number occurs on multiple lines you should print all of the lines in the order they occurred.
# If no line contains a number, your program should print nothing


# Format of number: [-]?[0-9]*[\.]?[0-9]+

@lines = (); # lines with number
@largest_numbers = (); # largest number for each line

while ($line = <STDIN>){
    # check whether the line contains number
    if ($line =~ /[-]?[0-9]*[\.]?[0-9]+/){
        # 这句比较重要! 将所有匹配结果组成arr
        @nums_inline = ($line =~ /([-]?[0-9]*[\.]?[0-9]+)/g);
        @nums_inline = sort{$b <=> $a}(@nums_inline);
        $largest_number = $nums_inline[0];
        push @lines, $line; # push curr line into lines
        push @largest_numbers, $largest_number;
    }
}

# get largest number
@largest_values = sort{$b <=> $a}(@largest_numbers);
$largest_value = $largest_values[0];


# [TEST]
# print "Lines: @lines\n";
# print "Largest numbers: @largest_numbers\n";
# print "Largest value: $largest_value\n";

# print all lines with largest number
$num_lines = @lines;
$curr_index = 0;
while ($curr_index < $num_lines){
    $curr_line = $lines[$curr_index];
    $curr_largest_number = $largest_numbers[$curr_index];
    if ($curr_largest_number == $largest_value){
        print "$curr_line";
    }
    $curr_index++;
}
