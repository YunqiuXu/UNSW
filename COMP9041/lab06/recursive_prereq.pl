#!/usr/bin/perl -w
# recursive version of prereq

# if there are 2 parameters: -r course_name: recursive
# else: same to prereq.pl

$num_args = @ARGV;
if ($num_args == 2){
    %pre = get_prereq_rec($ARGV[1]);
}
else{
    %pre = get_prereq($ARGV[0]);
}

@courses = keys %pre;
@courses = sort(@courses);

foreach $course(@courses){
    print "$course\n";
}


# non-recursive
# input: a course
# output: a hash list with its direct prerequisites
sub get_prereq{
    my $keyword = $_[0];
    
    my $under_url = "http://www.handbook.unsw.edu.au/undergraduate/courses/current/$keyword.html";
    my $post_url = "http://www.handbook.unsw.edu.au/postgraduate/courses/current/$keyword.html";
    
    open DATA, "wget -q -O- $under_url $post_url |" or die;
    my %pre = (); # just current result
    while (my $line = <DATA>) {
        if ( $line =~ m/Prerequisite/ ){
            $line =~ s/strong.*?$//g;
            my $head_index = 0;
            my $line_length = length $line;
            while ($head_index <= $line_length - 8){
                my $word = substr($line, $head_index, 8);
                if ($word =~ m/^[A-Z]{4}[0-9]{4}$/ and not exists($pre{$word})){
                    $pre{$word} = 1;                  
                }
                $head_index++;
            }
        }
    }
    
    return %pre;
}


# recursive
# input: a course
# output: a hash list including all its prerequisites recursively
sub get_prereq_rec{
    my $keyword = $_[0];
    
    # print "Current course : $keyword\n";
    
    my %pre = get_prereq($keyword); # get the direct prereq for this course
    
    my @courses = keys %pre;
    
    # print "Prereq for $keyword: @courses\n";
    
    # insert courses into %pre, they will not repeat with each other
    foreach my $course(@courses){
        $pre{$course} = 1; 
    }
    
    # then find their sub courses recursively
    foreach my $course(@courses){
        my %subpre = get_prereq_rec($course);
        my @subcourses = keys %subpre;
        foreach my $subcourse(@subcourses){
            if(not exists($pre{$subcourse})){
                $pre{$subcourse} = 1;
            }
        }
    }
    
    return %pre;
}
