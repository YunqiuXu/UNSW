#!/usr/bin/perl -w
# [PASSED]
# if $ARGV[0] == -d --> display hours

if ($ARGV[0] =~ /^-d$/){
    $start_position = 1;
}
else{
    $start_position = 0;
}
$length = @ARGV;

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
            exit 0;
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
        if ($start_position == 1){
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
        else{
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
        if ($start_position == 1){
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
        else{
            foreach $lec_time(@s2_lec){
                print "$course: S2 $lec_time";
            }
        }
    }
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

