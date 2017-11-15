#!/usr/bin/perl -w


###############################################################################
#                        COMP9041 Assignment 01                               #
#                     Author : Yunqiu Xu (z5096489)                           # 
#                                                                             # 
###############################################################################




###############################################################################
#    Main part                                                                #
###############################################################################

@lines = ();
# Collect all inputs
while ($line = <STDIN>){
    # Remove \n in the end
    chomp $line; 
    # Check interpreter and modules
    $line = change_head($line);
    push @lines, $line;
}
# Perform major transformations
@lines = transform(@lines);
# Load perl packages
$package_line = "use POSIX \'floor\';";
splice(@lines, 1, 0, $package_line);
# Output
foreach $line(@lines){
    print "$line\n";
}




###############################################################################
#    Functions                                                                #
###############################################################################

# Function : change_head
# Check head interpreter and python modules
#   Change python head interpreter to perl
#   If there are python modules imported, skip them
sub change_head{
    my $line = $_[0];
    # Case 1: change interpreter
    if ($line =~ m/^#!/ && $. == 1){        
        $line = "#!/usr/bin/perl -w";
    }
    # Case 2: skip import
    elsif ($line =~ m/^import/){
        $line = "";
    }
    return $line;
}


# Function : transform(line)
# Perform major transformations
# Input : an array of all lines
# Output : transformed lines
sub transform{
    my @transformed_lines = ();
    my @original_lines = @_;
    my $num_lines = @original_lines;
    my $curr_index = 0;

    while ($curr_index < $num_lines){
        my $line = $original_lines[$curr_index];

        # Case 1: skip comments
        if ($line =~ m/^[\s\t]*#/){
            push @transformed_lines, $line;
            $curr_index += 1;
        }
        # Case 2: single line statement, e.g. if/while/for
        elsif ($line =~ m/^[\s\t]*(if|while|for)[\s\t]*.*:([^:]*[^\s\t:]+[^:]*)$/){
            $line = change_statement_singleline($line);
            push @transformed_lines, $line;
            $curr_index += 1;
        }
        # Case 3: multi-line statement, e.g. if/elif/else/while/for
        elsif ($line =~ m/^[\s\t]*(if|elif|else|while|for)[\s\t]*.*:[\s\t]*$/){            
            # Modify current line
            $line = change_statement_multiline($line);
            push @transformed_lines, $line;
            $curr_index += 1;
            # Get indents of next line
            my $num_indents = 0; 
            my $sub_line = $original_lines[$curr_index];
            if ($sub_line =~ m/^([\s\t]+).*$/){
                $num_indents = length $1;
            }
            # Collect all lines with same or more indents as @sublines
            my @sub_lines = ();
            while ($curr_index < $num_lines){
                $sub_line = $original_lines[$curr_index];
                if ($sub_line =~ m/^([\s\t]+).*$/){
                    my $curr_indents = length $1;
                    if ($curr_indents >= $num_indents){
                        my $sub_line_length = length $sub_line;
                        # Remove indents
                        $sub_line = substr($sub_line, $num_indents, $sub_line_length - $num_indents);
                        push @sub_lines, $sub_line;
                    }
                    # Less indents, break subloop
                    else{ 
                        last;
                    }
                }
                # No indent, break subloop
                else{ 
                    last;
                }
                $curr_index += 1;
            }
            # Perform transformation recursively
            @sub_lines = transform(@sub_lines);
            # Add indents to result
            foreach my $ll (@sub_lines){
                $ll = "    $ll";
                push @transformed_lines, $ll;
            }
            # Add end line
            push @transformed_lines, "}";            
        }
        # Case 4: dict
        elsif ($line =~ m/^[^\"\']*[^A-Za-z0-9_]+[\s\t]*\{.*\}[^\"\']*/){            
            $line = change_dict($line);
            push @transformed_lines, $line;
            $curr_index += 1;
        }
        # Case 5: list or iterable objects
        elsif ($line =~ m/^[^\"\']*([^A-Za-z0-9_]+[\s\t]*\[.*\]|sys\.stdin\.readlines\(\)|sorted\(.*?\))[^\"\']*$|[^\"\']*[A-Za-z0-9_]+\[.*?:.*?\][^\"\']*/ and $line !~ m/join/){
            $line = change_list($line);
            push @transformed_lines, $line;
            $curr_index += 1;
        }
        # Case 6: general case 
        else{
            $line = change_print($line);
            $line = change_append_and_pop($line);
            $line = change_assignment($line);
            $line = change_continue_break($line);
            push @transformed_lines, $line;
            $curr_index += 1;
        }
    }
    return @transformed_lines;
}


# Function: change_statement_singleline()
# Detect and transform singleline statement
sub change_statement_singleline{
    my $line = $_[0];

    # Case 1: "if/while logical_expression : contents"
    if ($line =~ m/^[\s\t]*(if|while)[\s\t]+(.*):([^:]*[^\s\t:]+[^:]*)$/){
        # Get statement
        my $statement = $1;
        # Modify logical expression
        my $logical = $2;
        $logical = change_logic($logical);
        # Modify contents
        my @contents = split(";", $3);
        my $result_content = "";
        foreach my $content (@contents){
            $content = change_continue_break($content);
            $content = change_print($content);
            $content = change_assignment($content);
            $result_content = "$result_content$content ";
        }
        # Combine result
        $line = "$statement ( $logical ) {$result_content}";
    }
    # Case 2: "for variable in iterable : contents"
    elsif ($line =~ m/^[\s\t]*for[\s\t]+(.*?)[\s\t]+in[\s\t]+(.*):([^:]*[^\s\t:]+[^:]*)$/){
        # Modify variable
        my $var = $1;
        $var = change_computation($var);
        # Modify iterable object
        my $iterable = $2;
        $iterable = change_iterable($iterable);
        # Modify contents
        my @contents = split(";", $3);
        my $result_content = "";
        foreach my $content (@contents){
            $content = change_continue_break($content);
            $content = change_print($content);
            $content = change_assignment($content);
            $result_content = "$result_content$content ";
        }
        # Combine result
        $line = "foreach $var ($iterable) {$result_content}";
    }

    return $line;
}


# Function: change_statement_multiline()
# Detect and transform multiline statement
sub change_statement_multiline{
    my $line = $_[0];

    # Case 1: "if/while logical_expression : "
    if ($line =~ m/^[\s\t]*(if|while)[\s\t]+(.*):[\s\t]*$/){
        my $statement = $1;
        my $logical = $2;
        $logical = change_logic($logical);
        $line = "$statement ( $logical ) {";
    }
    # Case 2: "elif logical_expression : "
    if ($line =~ m/^[\s\t]*elif[\s\t]+(.*):[\s\t]*$/){
        my $logical = $1;
        $logical = change_logic($logical);
        $line = "elsif ( $logical ) {";
    }
    # Case 3: "else :"
    elsif ($line =~ m/^[\s\t]*(else)[\s\t]*:[\s\t]*$/){
        $line = "$1 {";
    }
    # Case 4: "for variable in fileinput.input() : "
    elsif ($line =~ m/^[\s\t]*for[\s\t]+(.*?)[\s\t]+in[\s\t]+fileinput\.input\(\):[\s\t]*$/){
        my $var = $1;
        $var = change_computation($var);
        $line = "while ($var = <>) {";
    }
    # Case 5: "for variable in iterable : "
    elsif ($line =~ m/^[\s\t]*for[\s\t]+(.*?)[\s\t]+in[\s\t]+(.*):[\s\t]*$/){
        my $var = $1;
        $var = change_computation($var);
        my $iterable = $2;
        $iterable = change_iterable($iterable);
        $line = "foreach $var ($iterable) {";
    }
    return $line;
}


# Function: change_logic
# Detect and transform logical expressions
sub change_logic{
    my $line = $_[0];

    # Case 1: "key (not) in dict"
    if ($line =~ m/^(.*?)[\s\t\(\)]+(not in|in)[\s\t\(\)]+(.*?)$/){
        my $key = $1;
        $key = change_computation($key);
        my $logic_operator = $2;
        my $dic = $3;
        $line = "exists (\$$dic\{$key\})";
        # Case : not in
        if ($logic_operator =~ m/^not in$/){
            $line = "not $line";
        }
        return $line;
    }
    # Case 2: "left_expression and/or/not right_expression"
    elsif ($line =~ /^(.*?[\s\t\(\)]+)(and|or|not)([\s\t\(\)]+.*?)$/){
        # Get left and right expressions, and connection operatior
        my $left = $1;
        my $logic_operator = $2;
        my $right = $3;
        # Perform transformation recursively on left and right expression
        $left = change_logic($left);
        $right = change_logic($right);
        # Combine result
        $line = "$left $logic_operator $right";
    }
    # Case 3: "left_expression comparision_operator right_expression"
    elsif ($line =~ m/^(.*?[\s\t\(\)]+)(>=|<=|==|!=|>|<)([\s\t\(\)]+.*?)$/){
        # Get left and right expressions, and connection operatior
        my $left = $1;
        my $logic_operator = $2;
        my $right = $3;
        # Perform transformation recursively on left and right expression
        $left = change_logic($left);
        $right = change_logic($right);
        # Combine result
        $line = "$left $logic_operator $right";
    }
    # Case 4: general cases
    else{
        $line = change_computation($line);
    }

    return $line;
}


# Function: change_continue_break
# Detect and transform "continue" and "break"
sub change_continue_break{
    my $line = $_[0];
    # Case 1: continue
    if ($line =~ m/^[\s\t]*continue[\s\t]*$/){
        $line = "next;";
    }
    # Case 2: break
    elsif ($line =~ m/^[\s\t]*break[\s\t]*$/){
        $line = "last;";
    }
    return $line;
}


# Function: change_list()
# Detect and transform list difinition
sub change_list{
    my $line = $_[0];

    # Case 1: basic list difinition, "var = [contents]"
    if ($line =~ m/^[\s\t]*(.*?)[\s\t]*=[\s\t]*\[(.*)\]/){
        # Modify variable as list name
        my $var = $1;
        $var = "\@$var";
        # Modify contents in "[]"
        my @contents = split(',', $2);
        my @result_contents = ();
        foreach my $content (@contents){
            $content = change_computation($content);
            push @result_contents, $content;
        }
        # Combine result
        my $result = join(', ', @result_contents);
        $line = "$var = ($result);";
    }
    # Case 2: "var = sys.stdin.readlines()"
    elsif ($line =~ m/^[\s\t]*(.*?)[\s\t]*=[\s\t]*sys\.stdin\.readlines\(\)/){
        my $var = $1;
        $var = "\@$var";
        $line = "$var = (); while(\$temp_var = <STDIN>){ push $var,\$temp_var; };";
    }
    # Case 3: "var = sorted(iterable)"
    elsif ($line =~ m/^[\s\t]*(.*?)[\s\t]*=[\s\t]*(sorted\(.*?\))/){
        my $var = $1;
        $var = "\@$var";
        my $iterable = $2;
        $iterable = change_iterable($iterable);
        $line = "$var = $iterable;";
    }
    # Case 4: "var = sys.argv[left:right]"
    elsif ($line =~ m/^[\s\t]*(.*?)[\s\t]*=[\s\t]*(sys\.argv\[.*?:.*?\])/){
        my $var = $1;
        $var = "\@$var";
        my $iterable = $2;
        $iterable = change_iterable($contents);
        $line = "$var = $iterable;";
    }
    # Case 5: "var = arr_name[left:right]"
    elsif ($line =~ m/^[\s\t]*(.*?)[\s\t]*=[\s\t]*([A-Za-z0-9_]+\[.*?:.*?\])/){
        my $var = $1;
        $var = "\@$var";
        my $iterable = $2; 
        $iterable = change_iterable($iterable);
        $line = "$var = $contents;";
    }
    
    return $line;
}


# Function: change_iterable()
# Detect and transform iterable objects
sub change_iterable{
    my $line = $_[0];
    
    # Case 1: "range(lower, upper)"
    if ($line =~ m/range\((.*?),(.*)\)/){
        my $lower = $1;
        my $upper = $2;
        $lower = change_computation($lower);
        $upper = change_computation($upper);
        $line = "($lower..$upper-1)";
    }
    # Case 2: "range(upper)"
    elsif ($line =~ m/range\((.*)\)/){
        my $upper = $1;
        $upper = change_computation($upper);
        $line = "(0..$upper-1)";
    }
    # Case 3: "sys.stdin", "sys.stdin.readlines()"
    elsif ($line =~ m/sys\.stdin/){
        $line = "<STDIN>";
    }
    # Case 4: "sorted(list)"
    elsif ($line =~ m/sorted\((.*)\)/){
        $line = "sort(\@$1)";
    }
    # Case 5: "sys.argv[left:right]"
    elsif ($line =~ m/sys\.argv\[(.*?):(.*?)\]/){
        my $arr_name = "ARGV";
        my $left = $1;
        my $right = $2;
        # Check right bound
        if ($right =~ m/^[\s\t]*$/){
            $right = "\$#$arr_name+1";
        }
        elsif ($right =~ m/-([0-9]+)/){
            $right = "\$#$arr_name+1-$1";
        }
        else {
            $right = change_computation($right);
        }
        # Check left bound
        if ($left =~ m/-([0-9]+)/){
            $left = "\$#$arr_name+1-$1";
            $line = "\@$arr_name\[$left..$right-1\]";
        }
        else {
            $left = change_computation($left);
            $line = "\@$arr_name\[$left-1..$right-1\]";
        }
    }
    # Case 6: "arr_name[left:right]"
    elsif ($line =~ m/([A-Za-z0-9_]+)\[(.*?):(.*?)\]/){
        my $arr_name = $1;
        my $left = $2;
        my $right = $3;
        # Check left bound
        if ($left =~ m/^[\s\t]*$/){
            $left = 0;
        }
        elsif ($left =~ m/-([0-9]+)/){
            $left = "\$#$arr_name+1-$1";
        }
        else {
            $left = change_computation($left);
        }
        # Check right bound
        if ($right =~ m/^[\s\t]*$/){
            $right = "\$#$arr_name+1";
        }
        elsif ($right =~ m/-([0-9]+)/){
            $right = "\$#$arr_name+1-$1";
        }
        else {
            $right = change_computation($right);
        }
        $line = "\@$arr_name\[$left..$right-1\]";
    }
    # Case 7: general iterable objects
    else{
        $line = "\@$line";
    }

    return $line;
}


# Function: change_append_and_pop()
# Detect list append and pop operations
sub change_append_and_pop{
    my $line = $_[0];
    # Case 1: append
    if ( $line =~ m/([A-Za-z0-9_]+)\.append\((.*)\)/){
        my $arr = $1;
        $arr = "\@$arr";
        my $contents = $2;
        $contents = change_computation($contents);
        $line = "push($arr, $contents);";
    }
    # Case 2: pop
    elsif ($line =~ m/^([A-Za-z0-9_]+)\.pop\((.*)\)/){
        my $arr = $1;
        $arr = "\@$arr";
        # Handle "pop(index)"
        my $pop_index = $2;
        if ($pop_index =~ m/^[0-9]+$/){
            $line = "splice($arr, $pop_index, 1);";
        }
        else{
            $line = "pop($arr);";
        }
    }
    return $line;
}


# Function: change_dict()
# Detect and transform dict
sub change_dict{
    my $line = $_[0];
    if ($line =~ m/^[\s\t]*(.*?)[\s\t]*=[\s\t]*\{(.*)\}/){
        my $var = $1;
        $var = "\%$var";
        my $contents = $2;
        $contents =~ tr/:/,/;
        $line = "$var = ($contents);";
    }
    return $line;
}


# Function: change_print()
# Detect and transform print()
sub change_print{
    my $line = $_[0];

    # Case 1: print()
    if ($line =~ m/^[\s\t]*print[\s\t]*\([\s\t]*\)$/){
        $line = "print \"\\n\";";
    }
    # Case 2: print("string", end)
    elsif ($line =~ m/^[\s\t]*print[\s\t]*\([\s\t]*\"(.*)\"[\s\t]*,[\s\t]*end[\s\t]*=[\s\t]*\'(.*?)\'\)$/){
        $line = "print \"$1$2\";";
    }
    # Case 3: print("string")
    elsif ($line =~ m/^[\s\t]*print[\s\t]*\([\s\t]*\"(.*)\"[\s\t]*\)$/){
        $line = "print \"$1\\n\";";
    }
    # Case 4: print string with format, print("string"%(vars))
    elsif ($line =~ m/^[\s\t]*print[\s\t]*\([\s\t]*\"(.*)\"[\s\t]*[\s\t]*%[\s\t]*(.*)[\s\t]*\)$/){
        # Get string and variables
        my $string = $1;
        $string = "printf \"$1\\n\",";
        my $vars = $2;
        my $result_vars = "";
        # Check whether there are multiple variables
        if ($vars =~ m/^\((.*)\)$/){
            my $vars = $1;
            my @vars_list = split(',', $vars);
            my @result_list = ();
            foreach my $var (@vars_list){
                $var = change_computation($var);
                push @result_list, $var;
            }
            $result_vars = join(', ', @result_list);
        } 
        # Single variable
        elsif ($vars =~ m/^([A-Za-z0-9_]+)$/){
            $result_vars = "\$$1";
        }
        # Combine result
        $line = "$string $result_vars;";
    }
    # Case 5: print(variable_expression, end)
    elsif ($line =~ m/^[\s\t]*print[\s\t]*\([\s\t]*(.*)[\s\t]*,[\s\t]*end[\s\t]*=[\s\t]*\'(.*?)\'\)$/){
        my $expression = $1;
        $expression = change_computation($expression);
        $line = "print $expression, \"$2\";"; 
    }
    # Case 6: print(variable_expression)
    elsif ($line =~ m/^[\s\t]*print[\s\t]*\([\s\t]*(.*)[\s\t]*\)$/){
        my $expression = $1;
        $expression = change_computation($expression);
        $line = "print $expression, \"\\n\";"; 
    }
    # Case 7: sys.stdout.write()
    elsif ($line =~ m/^[\s\t]*sys\.stdout\.write[\s\t]*\([\s\t]*\"(.*)\"[\s\t]*\)$/){
        $line = "print \"$1\";";
    }
    
    return $line;
}


# Function: change_assignment
# Detect and transform general variable assignment
# Split by "=" or others, then transform left part and right part
sub change_assignment{
    my $line = $_[0];

    # Case 1: var = re.sub(raw, rep, var)
    if ($line =~ m/^([\s\t]*)([A-Za-z0-9_]+)[\s\t]*=[\s\t]*re\.sub\(r\'(.*)\',[\s\t]*\'(.*)\',(.*?)\)[\s\t]*$/){
        my $spaces = $1;
        my $raw = $3;
        my $rep = $4;
        my $var = $5;
        $var = change_computation($var);
        $line = "$spaces$var =~ s/$raw/$rep/g;"
    }
    # Case 2: var = re.sub(raw, rep, var), here var contains "[]", e.g. num[i]
    elsif ($line =~ m/^([\s\t]*)([A-Za-z0-9_]+\[.*?\])[\s\t]*=[\s\t]*re\.sub\(r\'(.*)\',[\s\t]*\'(.*)\',(.*?)\)[\s\t]*$/){
        my $spaces = $1;
        my $raw = $3;
        my $rep = $4;
        my $var = $5;
        $var = change_computation($var);
        $line = "$spaces$var =~ s/$raw/$rep/g;"
    }
    # Case 3: left = right
    elsif ($line =~ m/^([\s\t]*)([A-Za-z0-9_]+)[\s\t]*=[\s\t]*(.*?)[\s\t]*$/){
        my $spaces = $1;
        my $left = $2;
        $left = change_computation($left);
        my $right = $3;        
        $right = change_computation($right);
        $line = "$spaces$left = $right;";
    }
    # Case 4: left = right, here left contains "[]"
    elsif ($line =~ m/^([\s\t]*)([A-Za-z0-9_]+\[.*?\])[\s\t]*=[\s\t]*(.*?)[\s\t]*$/){
        my $spaces = $1;
        my $left = $2;
        $left = change_computation($left);
        my $right = $3;        
        $right = change_computation($right);
        $line = "$spaces$left = $right;";
    }
    # Case 5: //=, **=
    # left **= right --> $left = $left ** $right
    elsif ($line =~ m/^([\s\t]*)([A-Za-z0-9_]+)[\s\t]*(\*\*=|\/\/=)[\s\t]*(.*?)[\s\t]*$/){
        my $spaces = $1;
        my $left = $2;
        my $new_operator = substr($3, 0, 2);
        my $right = "$left $new_operator ( $4 )";
        $left = change_computation($left);
        $right = change_computation($right);
        $line = "$spaces$left = $right;";
    }
    # Case 6: //=, **=, here left contains "[]"
    elsif ($line =~ m/^([\s\t]*)([A-Za-z0-9_]+\[.*?\])[\s\t]*(\*\*=|\/\/=)[\s\t]*(.*?)[\s\t]*$/){
        my $spaces = $1;
        my $left = $2;
        my $new_operator = substr($3, 0, 2);
        my $right = "$left $new_operator ( $4 )";
        $left = change_computation($left);
        $right = change_computation($right);
        $line = "$spaces$left = $right;";
    }
    # Case 7: +=, -=, *=, /=, %=
    elsif ($line =~ m/^([\s\t]*)([A-Za-z0-9_]+)[\s\t]*(\+=|-=|\*=|\/=|%=)[\s\t]*(.*?)[\s\t]*$/){
        my $spaces = $1;
        my $left = $2;
        my $new_operator = substr($3, 0, 1);
        my $right = "$left $new_operator ( $4 )";
        $left = change_computation($left);
        $right = change_computation($right);
        $line = "$spaces$left = $right;";
    }
    # Case 8: +=, -=, *=, /=, %=, here left contains "[]"
    elsif ($line =~ m/^([\s\t]*)([A-Za-z0-9_]+\[.*?\])[\s\t]*(\+=|-=|\*=|\/=|%=)[\s\t]*(.*?)[\s\t]*$/){
        my $spaces = $1;
        my $left = $2;
        my $new_operator = substr($3, 0, 1);
        my $right = "$left $new_operator ( $4 )";
        $left = change_computation($left);
        $right = change_computation($right);
        $line = "$spaces$left = $right;";
    }
    
    return $line;
}


# Function: change_computatiion
# Transform general non-iterable variable expression
# "x + y - 1" --> "x+y-1" --> ($x), "+y-1" --> ... --> ($x,+,$y,-,1) --> "$x + $y - 1"
sub change_computation{
    # Keywords
    my %keywords = ('print', 1, 'and',1 , 'or', 1, 'not', 1, 'if', 1, 'elif', 1, 'else', 1, 'while', 1, 'for', 1, 'in', 1, 'break', 1, 'continue', 1, 'range', 1, 'import', 1, "sys.", 1, "int", 1, "list", 1, "append", 1, "push", 1, "pop", 1, "len", 1, "join", 1, "split", 1, "stdin", 1, "stdout", 1, "input", 1, "argv", 1);
    my $line = $_[0];

    # Case 1: string
    if ($line =~ m/^[\s\t]*[\"\'].*[\"\'][\s\t]*$/){
        return $line;
    }
    # Case 2: 'connector'.join(iterable)
    if ($line =~ m/^[\s\t]*[\"\'](.*)[\"\']\.join\((.*)\)[\s\t]*$/){
        my $connector = $1;
        my $iterable = $2;
        $iterable = change_iterable($iterable);
        $line = "join(\"$connector\", $iterable)";
        return $line;
    }

    # Remove all spaces
    $line =~ s/[\s\t]+//g; 
    # Get the length of line for iteration
    my $curr_length = length $line;
    # Store all elements
    my @elements = ();

    while ($curr_length != 0){
        # Initialize current element length
        my $curr_element_length = 0;
        
        # Case 3: a // b --> floor a / b
        if ($line =~ m/^(\/\/)/){
            $curr_element_length = length $1;
            my $change = "\/";
            push @elements, $change;
            unshift @elements, 'floor';
        }
        # Case 4: +, -, %, **, *, /, (, )
        elsif ($line =~ m/^(\+|-|%|(\*\*)|\*|\/|\(|\))/){

            $curr_element_length = length $1;
            push @elements, $1;

        }
        # Case 5: bitwise operators | ^ & << >> ~
        elsif ($line =~ m/^(\||\^|&|<<|>>|~)/){
            $curr_element_length = length $1;
            push @elements, $1;
            # Handle priority: a ^ b --> ($a ^ $b)
            unshift @elements, '(';
            $line = "$line" . ")"; 
            $curr_length = length $line;
        }
        # Case 6: int(variable)
        elsif ($line =~ m/^(int)/){
            $curr_element_length = length $1;
            push @elements, $1;
        }
        # Case 7: sys.stdin.readline() --> <STDIN>
        elsif ($line =~ m/^(sys\.stdin\.readline\(\))/){
            $curr_element_length = length $1;
            push @elements, "<STDIN>";
        }
        # Case 8: constants
        elsif ($line =~ m/^([0-9]+[\.]*[0-9]*)/){
            $curr_element_length = length $1;
            push @elements, $1;
        }
        # Case 9: sys.argv[index]
        elsif ($line =~ m/^sys\.argv\[([-]*)([0-9a-zA-Z_]+)\]/){
            $curr_element_length = length($1) + length($2) + 10;
            my $arr_name = "ARGV";
            my $neg = $1;
            my $index = $2;
            $index = change_computation($index);
            # Check whether the index is negative
            if ($neg =~ m/-/){

                $index = "\$#$arr_name+1-$index";
            }
            else{
                $index = "$index - 1";
            }
            my $change = "\$$arr_name\[$index\]";
            push @elements, $change;
        }
        # Case 10: list[index]
        elsif ($line =~ m/^([A-Za-z0-9_]+)\[([-]*)([^\[\]:]+?)\]/){
            $curr_element_length = length($1) + length($2) + length($3) + 2;
            my $arr_name = $1;
            my $neg = $2;
            my $index = $3;
            $index = change_computation($index);
            # Check whether the index is negative
            if ($neg =~ m/-/){
                $index = "\$#$arr_name+1-$index";
            }
            my $change = "\$$arr_name\[$index\]";
            push @elements, $change;
        }
        # Case 11: list.pop()
        elsif ($line =~ m/^([A-Za-z0-9_]+\.pop\(.*?\))/){
            $curr_element_length = length $1;
            my $change = $1;
            $change = change_append_and_pop($change);
            # remove ";"
            chop $change;
            push @elements, $change;
        }
        # Case 12: len(list)
        elsif ($line =~ m/^len\((.*?)\)/){
            $curr_element_length = length($1) + 5;
            my $arr_name = $1;
            my $change = "";
            # Handle special case: len(sys.argv)
            if ($arr_name =~ /^sys\.argv$/){
                $arr_name = "ARGV";
                $change = "\$\#$arr_name + 2";
            }
            else{
                $change = "\$\#$arr_name + 1";
            }
            push @elements, $change;
        }
        # Case 13: general non-iterable variables
        elsif ($line =~ m/^([A-Za-z0-9_]+)/){
            $curr_element_length = length $1;
            my $change = $1;
            if (not exists($keywords{$change})) {
                $change = "\$" . "$1";
            }
            push @elements, $change;
        }
        
        # Remove detected element from line, loop until there is no element
        $line = substr($line, $curr_element_length, $curr_length - $curr_element_length);
        $curr_length = length $line;
    }
    # Combine result
    $line = join(' ', @elements);
    return $line;
}




