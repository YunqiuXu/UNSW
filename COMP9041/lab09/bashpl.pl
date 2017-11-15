#!/usr/bin/perl -w

# take a Bash script as input and outputs an equivalent Perl program
# sum.sh [passed]
# double.sh [passed]
# pythagorean_triple.sh [passed]
# collatz.sh [passed]
# autotest [passed]


# Function: change the head
# head is the 1st line
# #!/bin/bash --> #!/usr/bin/perl -w
sub change_head{
    my $line = $_[0];
    if ($line =~ m/^#!\/bin\/bash|^#!\/bin\/sh/){
        $line = "#!/usr/bin/perl -w"
    }
    return $line;
}


# Function: change variable assignment
# case 1: a=1
# case 2: a=$((a+b))
# case 3: a=$b
sub change_assign{
    my $line = $_[0];
    if ($line =~ m/^[a-zA-Z]+[a-zA-Z_0-9]*=/){
        $line =~ s/\s+//g;
        $line =~ s/\(+//g;
        $line =~ s/\)+//g;
        $line =~ s/\$+//g;
        my @splitted = split('=', $line);
        $left = $splitted[0];
        $right = $splitted[1];

        # TEST

        $left = change_computation($left);
        $right = change_computation($right);

        $line = "$left=$right;";
    }
    return $line;
}


# Function: change if else
# if / elif / else
sub change_ifelse{
    my $line = $_[0];
    $line =~ s/\s+//g;
    if ($line =~ m/^if/){
        $line =~ s/^if\(+//g;
        $line =~ s/\)+$//g;
        $line = change_logic($line);
        $line = "if($line){"; 
    }
    elsif ($line =~ m/^elif/){
        $line =~ s/^elif\(+//g;
        $line =~ s/\)+$//g;
        $line = change_logic($line);
        $line = "}elsif($line){"; 
    }
    elsif ($line =~ m/^else/){
        $line = "}else{"; 
    }
    elsif ($line =~ m/^then$/){
        $line = "";
    }
    elsif ($line =~ m/^fi$/){
        $line = "}";
    }
    return $line;
}


# Function: change while loop
# while ((i <= finish)) --> while ($i <= $finish){
# do --> null
# done --> }
##### [Further] unimplemented
# while (( (i + 2) * j <= k ))
sub change_while{
    my $line = $_[0];
    $line =~ s/\s+//g; # remove all spaces
    if ($line =~ m/^while/){
        $line =~ s/^while\(+//g; # remove "while(("
        $line =~ s/\)+$//g; # remove )

        $line = change_logic($line);
        $line = "while($line){"; 
    }
    elsif ($line =~ m/^do$/){
        $line = "";
    }
    elsif ($line =~ m/^done$/){
        $line = "}";
    }

    return $line;
}


# Sub sub function
# Function: change logic
# a+b>c --> $a+$b>$c
# logics: >= <= == != > < 
sub change_logic{
    my $line = $_[0];
    if ($line =~ />=/){
        my @splitted = split('>=', $line);
        my $var1 = $splitted[0];
        my $var2 = $splitted[1];
        $var1 = change_computation($var1);
        $var2 = change_computation($var2);
        $line = "$var1>=$var2";
    }
    elsif($line =~ /<=/){
        my @splitted = split('<=', $line);
        my $var1 = $splitted[0];
        my $var2 = $splitted[1];
        $var1 = change_computation($var1);
        $var2 = change_computation($var2);
        $line = "$var1<=$var2";
    }
    elsif($line =~ /==/){
        my @splitted = split('==', $line);
        my $var1 = $splitted[0];
        my $var2 = $splitted[1];
        $var1 = change_computation($var1);
        $var2 = change_computation($var2);
        $line = "$var1==$var2";
    }
    elsif($line =~ /!=/){
        my @splitted = split('!=', $line);
        my $var1 = $splitted[0];
        my $var2 = $splitted[1];
        $var1 = change_computation($var1);
        $var2 = change_computation($var2);
        $line = "$var1!=$var2";
    }
    elsif($line =~ />/){
        my @splitted = split('>', $line);
        my $var1 = $splitted[0];
        my $var2 = $splitted[1];
        $var1 = change_computation($var1);
        $var2 = change_computation($var2);
        $line = "$var1>$var2";
    }
    elsif($line =~ /</){
        my @splitted = split('<', $line);
        my $var1 = $splitted[0];
        my $var2 = $splitted[1];
        $var1 = change_computation($var1);
        $var2 = change_computation($var2);
        $line = "$var1<$var2";
    }
    return $line;
}


# Sub sub function
# Function : change computation
# operators: + - * / %
# Case 1: a+b --> $a+$b
# Case 2: a*b+1/d --> $a*$b+1/$d
# Case 3: -1+a_1-b --> -1+$a_1-$b
##### [Thoughts]
# a*b+1/d --> (a,b,1,d),(*,+,/)
sub change_computation{
    my $line = $_[0];
    my @vars = split("[%\/\*\+\-]",$line);
    my @operators = split("[^%\/\*\+\-]+",$line);
    my $num_vars = @vars;
    my $num_operators = @operators;
    my $result = "";
    my $start_index = 0;
    if ($num_vars == 1){
        if ($line !~ /^[0-9]/){
            $result = '$' . "$line"
        }
        else{
            $result = $line;
        }
    }
    elsif ($num_vars > $num_operators){ # a + b + c
        while ($start_index < $num_operators){
            if ($vars[$start_index] !~ /^[0-9]/){
                $result = "$result" . '$' . "$vars[$start_index]" . "$operators[$start_index]";
            }
            else{
                $result = "$result" . "$vars[$start_index]" . "$operators[$start_index]";
            }
            $start_index++;
        }
        if ($vars[$start_index] !~ /^[0-9]/){
            $result = "$result" . '$' . "$vars[$start_index]";
        }
        else{
            $result = "$result" . "$vars[$start_index]";
        }
    }
    else{ # -a + b + c
        while ($start_index < $num_operators){
            if ($vars[$start_index] !~ /^[0-9]/){
                $result = "$result" . "$operators[$start_index]" . '$' . "$vars[$start_index]";
            }
            else{
                $result = "$result" . "$operators[$start_index]" . "$vars[$start_index]";
            }
            $start_index++;
        }
    }
    return $result;
}


# Function: change echo
sub change_echo{
    my $line = $_[0];
    if ($line =~ /^echo /){
        $line =~ s/echo /print \"/;
        $line = "$line" . "\\n\";";
    }
    return $line;
}


#################################################
# Main
open($DATA, '<', $ARGV[0]) or die("No such file, $!\n");
@lines = ();
$line_count = 0;
while ($line = <$DATA>){
    chomp $line;
    $line =~ s/^\s+//g; # remove spaces at head

    # transforming
    if ($line_count == 0){
        $line = change_head($line);
    }

    if ($line =~ /^echo /){
        $line = change_echo($line);
    }
    else{
        # $line = change_var_assign($line);
        # $line = change_var_compute($line);
        $line = change_ifelse($line);
        $line = change_while($line);
        $line = change_assign($line);
    }

    push @lines, $line;
    $line_count++;
}

foreach $line(@lines){
    print "$line\n";
}
