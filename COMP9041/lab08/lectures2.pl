#!/usr/bin/perl -w
# [PASSED]

# if $ARGV[0] == -d --> display
# if $ARGV[0] == -t --> table

if ($ARGV[0] =~ /^-[td]$/){
    $start_position = 1;
}
else{
    $start_position = 0;
}
$length = @ARGV;

%s1_table = (); # Key: day + start_time
%s2_table = (); # Value: repeat_time

foreach $course (@ARGV[$start_position..$length-1]){
    $url = "http://timetable.unsw.edu.au/current/" . $course .".html";
    open DATA, "wget -q -O- $url |" or die;

    $line = <DATA>;
    if (not $line){ # no match
        exit 0;
    }

    while ($line !~ /SUMMARY OF SEMESTER (ONE|TWO) CLASSES/){
        $line = <DATA>;
        if ($line =~ m/SEMESTER (ONE|TWO) CLASSES - Detail/){
            last;
        }
    }

    # check s1
    if ($line =~ /SUMMARY OF SEMESTER ONE CLASSES/){
        %s1 = ();
        while ($line !~ m/SUMMARY OF SEMESTER TWO CLASSES|SEMESTER (ONE|TWO) CLASSES - Detail/){
            $line = <DATA>;
            if($line =~ m/Lecture/){
                $count = 0;
                while ($count < 6){
                    $line = <DATA>;
                    $count++;
                }
                if($line =~ m/[A-Za-z]{3} [0-9]{2}:[0-9]{2}/){
                    $line =~ s/^.*data">//g;
                    $line =~ s/<\/td>$//g;
                    if(not exists($s1{$line})){
                        $s1{$line} = 1;
                    }
                }
            }
        }
        @s1_lec = sort (keys %s1);
        if ($ARGV[0] =~ m/^-d$/){ # display
            %final_repeated = ();
            foreach $lec_times(@s1_lec){
                @results = display($lec_times);
                foreach $result(@results){
                    if (not exists $final_repeated{$result}){
                        print "S1 $course $result\n";
                        $final_repeated{$result} = 1;
                    }
                }
            }
        }
        elsif ($ARGV[0] =~ m/^-t$/){ # table
            %final_repeated = ();
            foreach $lec_times(@s1_lec){
                @results = display($lec_times);
                foreach $result(@results){
                    if (not exists $final_repeated{$result}){
                        $final_repeated{$result} = 1;
                    }
                }
            }
            @final_repeated_keys = keys %final_repeated;
            foreach $result(@final_repeated_keys){
                if (not exists $s1_table{$result}){
                    $s1_table{$result} = 1;
                }
                else{
                    $s1_table{$result}++;
                }
            }
        }
        else {
            foreach $lec_time(@s1_lec){
                print "$course: S1 $lec_time";
            }
        }
    }

    # check s2
    if ($line =~ /SUMMARY OF SEMESTER TWO CLASSES/){
        %s2 = ();
        while ($line !~ m/SEMESTER (ONE|TWO) CLASSES - Detail/){
            $line = <DATA>;
            if($line =~ m/Lecture/){
                $count = 0;
                while ($count < 6){
                    $line = <DATA>;
                    $count++;
                }
                if($line =~ m/[A-Za-z]{3} [0-9]{2}:[0-9]{2}/){
                    $line =~ s/^.*data">//g;
                    $line =~ s/<\/td>$//g;
                    if(not exists($s2{$line})){
                        $s2{$line} = 1;
                    }
                }
            }
        }
        @s2_lec = sort (keys %s2);
        if ($ARGV[0] =~ m/^-d$/){ # display
            %final_repeated = ();
            foreach $lec_times(@s2_lec){
                @results = display($lec_times);
                foreach $result(@results){
                    if (not exists $final_repeated{$result}){
                        print "S2 $course $result\n";
                        $final_repeated{$result} = 1;
                    }
                }
            }
        }
        elsif ($ARGV[0] =~ m/^-t$/){ # table
            %final_repeated = ();
            foreach $lec_times(@s2_lec){
                @results = display($lec_times);
                foreach $result(@results){
                    if (not exists $final_repeated{$result}){
                        $final_repeated{$result} = 1;
                    }
                }
            }
            @final_repeated_keys = keys %final_repeated;
            foreach $result(@final_repeated_keys){
                if (not exists $s2_table{$result}){
                    $s2_table{$result} = 1;
                }
                else{
                    $s2_table{$result}++;
                }
            }
        }
        else {
            foreach $lec_time(@s2_lec){
                print "$course: S2 $lec_time";
            }
        }
    }
}

# Display the table
# xx:xx[\s]{5}Mon[\s]{5}Tue[\s]{5}Wed[\s]{5}[Thu][\s]{5}Fri
# If no course --> one space

# !!! UNCHANGED: if the number is larger than 10 --> alignment
# e.g. %6d


$s1_length = keys (%s1_table);
if ($ARGV[0] =~ m/^-t$/ and $s1_length != 0){

    @times = (9..20);
    @days = ("Mon", "Tue", "Wed", "Thu", "Fri");

    # print "Display S1\n";
    print "S1       Mon   Tue   Wed   Thu   Fri\n";
    # draw line by line
    foreach $curr_time (@times){
        if ($curr_time == 9){
            $curr_line = "09:00";
        }
        else{
            $curr_line = "$curr_time:00";
        }
        @Mon2Fri = ();
        foreach $curr_day (@days){
            $curr_key = "$curr_day" . " " . "$curr_time";
            if (exists $s1_table{$curr_key}){
                $curr_course = $s1_table{$curr_key};
            }
            else{
                $curr_course = " ";
            }
            push @Mon2Fri, $curr_course; # Mon Tue ...
        }
        printf "%s%6s%6s%6s%6s%6s\n", $curr_line, @Mon2Fri;
    }

    # print "S1 finished\n";
}

$s2_length = keys (%s2_table);
if ($ARGV[0] =~ m/^-t$/ and $s2_length != 0){
    @times = (9..20);
    @days = ("Mon", "Tue", "Wed", "Thu", "Fri");
    # print "Display S2\n";
    print "S2       Mon   Tue   Wed   Thu   Fri\n";
    # draw line by line
    foreach $curr_time (@times){
        if ($curr_time == 9){
            $curr_line = "09:00";
        }
        else{
            $curr_line = "$curr_time:00";
        }
        @Mon2Fri = ();
        foreach $curr_day (@days){
            $curr_key = "$curr_day" . " " . "$curr_time";
            if (exists $s2_table{$curr_key}){
                $curr_course = $s2_table{$curr_key};
            }
            else{
                $curr_course = " ";
            }
            push @Mon2Fri, $curr_course; # Mon Tue ...
        }
        printf "%s%6s%6s%6s%6s%6s\n", $curr_line, @Mon2Fri;
    }
    # print "S2 finished\n";
}





# Function : display($lec_times)
sub display{
   my @lec_times = split(', ', $_[0]);
   my %repeat_check = ();
   my @results= ();
   foreach my $lec_time(@lec_times){
       # print "$lec_time\n";
       my $day = substr($lec_time, 0, 3);
       my $start_time = int(substr($lec_time, 4, 2));
       my $end_time = int(substr($lec_time, 12, 2));
       # print "Start time : $start_time\n";
       # print "End time : $end_time\n";
       while ($start_time < $end_time){
           my $curr_key = "$day" . " " . "$start_time";
           # print "Curr key : $curr_key\n";
           if (not exists($repeat_check{$curr_key})){
               $repeat_check{$curr_key} = 1;
               push @results,$curr_key;
           }
           $start_time++;
       }
   }
   return @results;
}

