#!/usr/bin/perl -w

# read from stdin
# split the words by spaces
# lower case the word, check whether the word is equi-lettered
# rejoine the words by only one space

# 先把所有标准输入存起来
@lines = ();
while ($line = <STDIN>){
    push @lines, $line;
}

# 对每行, 先去掉换行符 -> 分割词汇 -> 检查每个词汇 -> 将结果变为字符串输出
foreach $line (@lines){
    chomp $line;
    @words = split(" +", $line);
    @result = ();
    foreach $word (@words){
        $flag = check_equal($word);

        # TEST
        # print "Flag for $word is $flag\n";

        if ($flag == 1){
            push @result,$word;
        }
    }
    $result_line = join(" ", @result);
    print "$result_line\n";
}

# if the word is equal-letters, return 1, else return 0
# 检查是否为equal-letter: 看是不是每个字母出现次数都相同
sub check_equal{
    my $word = $_[0];
    $word = lc $word;

    # if ($word !~ m/^[a-z]+$/){
    #     return 1;
    # }

    my @letters = split("", $word);
    my %letter_count = ();
    foreach my $letter(@letters){
        if (exists($letter_count{$letter})){
            $letter_count{$letter} += 1;
        }
        else{
            $letter_count{$letter} = 1;
        }
    }
    
    my @counts = values(%letter_count);
    my $check_flag = $counts[0];

    # TEST
    # print "Check flag : $check_flag\n";

    foreach my $count(@counts){

        # TEST
        # print "Current count : $count\n";

        if ($count != $check_flag){
            return 0;
        }
    }

    return 1;
}
