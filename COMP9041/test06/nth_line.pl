#!/usr/bin/perl -w
$line_num = $ARGV[0];
$file_name = $ARGV[1];
chomp $line_num; # 这里应该不需要chomp

open($DATA, '<', $file_name) or die ("Can not open file, $!");
$count = 0;
while($curr_line = <$DATA>){
    $count++;
    if ($count == $line_num){
        print "$curr_line";
        exit(0);
    }
}

