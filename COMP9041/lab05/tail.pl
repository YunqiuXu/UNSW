#!/usr/bin/perl -w

# Simulate tail command
# case 1: ./tail.pl <t1.txt
# case 2: ./tail.pl -5 <t1.txt
# case 3: t1.txt
# case 4: -5 t1.txt

$argv_length = @ARGV;
if($argv_length == 0){ # STDIN file
    get_tail_from_stdin(10);
    exit(0);
}

$first_argv = $ARGV[0];
if($first_argv =~ m/^-[0-9]*/){ # $line_num
    $tail_num = substr($first_argv,1, length($first_argv));
    
    if($argv_length == 1){
        get_tail_from_stdin($tail_num);
        exit(0);
    }
    $curr_argv_index = 1; # open file from next argv
}
else{
    $tail_num = 10;
    $curr_argv_index = 0;
}

$file_num = $argv_length - $curr_argv_index;
if($file_num == 1){
    $curr_file = $ARGV[$curr_argv_index];
    get_tail($curr_file, $tail_num);
    exit(0);
}
else{
    while($curr_argv_index < $argv_length){
        $curr_file = $ARGV[$curr_argv_index];
        print "==> " . $curr_file . " <==\n";
        get_tail($curr_file, $tail_num);
        $curr_argv_index++;
    }
}

## get_tail_from_stdin($tail_num)
## print the last $tail_num lines of stdin
sub get_tail_from_stdin{
    my @lines = ();
    while(my $line = <STDIN>){
        push @lines, $line;
    }
    
    # tail_num = min($line_num, $_[0])
    my $line_num = @lines;
    my $tail_num = $_[0] > $line_num ? $line_num : $_[0];
    my $curr = $line_num - $tail_num;
    
    while($curr < $line_num){
        my $curr_line = $lines[$curr];
        print "$curr_line";
        $curr++;
    }
}


## get_tail($file_name, $tail_num)
## print the last $tail_num lines of $file_name
sub get_tail{
    open(my $DATA, '<', $_[0]) or die ("$0: Can't open $_[0]: $!\n");
    my @lines = ();
    while(my $line = <$DATA>){
        push @lines, $line;
    }
    
    # tail_num = min($line_num, $_[1])
    my $line_num = @lines;
    my $tail_num = $_[1] > $line_num ? $line_num : $_[1];
    my $curr = $line_num - $tail_num;
    
    while($curr < $line_num){
        my $curr_line = $lines[$curr];
        print "$curr_line";
        $curr++;
    }
}
            
