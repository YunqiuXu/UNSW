#!/usr/bin/perl -w

# If the file contains an odd number of lines it should print one line
# If the file contains an even number of lines it should print two lines
# If the file contains no lines it should print nothing

$file = $ARGV[0];
open($DATA, '<', $file) or die("/bin/sh: ./middle_lines.pl: $!\n");

@lines = ();
while($line = <$DATA>){
    push @lines, $line;
}

# 可以直接用 if(!@lines) 判断是否输入为零
$line_num = @lines; # $#lines + 1
$mod = $line_num % 2;
$middle = $line_num / 2;

if ($line_num > 0 && $mod != 0){ # odd
    print "$lines[$middle]";
}

if ($line_num > 0 && $mod == 0){ # even
    print "$lines[$middle-1]";
    print "$lines[$middle]";
}
