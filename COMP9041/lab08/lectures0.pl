#!/usr/bin/perl -w
# [PASSED]

# Only lecture, no lab / tutorial
# Don't print identical lecture streams (where times & weeks are identical) multiple times.

# SUMMARY OF SEMESTER ONE CLASSES
# SUMMARY OF SEMESTER TWO CLASSES
# SEMESTER ONE CLASSES - Detail | SEMESTER TWO CLASSES - Detail
# The 6th line behind "Lecture"
# Format of time:  <td class="data">Tue 18:00 - 21:00 (Weeks:1-7,8-12), Tue 18:00 - 21:00 (Weeks:13)</td>


foreach $course (@ARGV){
    $url = "http://timetable.unsw.edu.au/current/" . $course .".html";
    open DATA, "wget -q -O- $url |" or die;

    $line = <DATA>;
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
        foreach $lec_time(@s1_lec){
            print "$course: S1 $lec_time";
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
        foreach $lec_time(@s2_lec){
            print "$course: S2 $lec_time";
        }
    }
    
    
}
