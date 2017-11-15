#!/usr/bin/perl -w

# replace [01234] as <, replace [6789] as >
@arr = ();
while($item = <STDIN>){
    push(@arr, $item);
}
# 可以直接简化为 @arr = <>


foreach $item(@arr){
    $item =~ s/[01234]/\</g;
	$item =~ s/[6789]/\>/g;
	print STDOUT $item; # 其实不需要STDOUT这个
}

