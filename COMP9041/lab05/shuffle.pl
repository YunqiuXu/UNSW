#!/usr/bin/perl -w

@arr = ();
while($item = <STDIN>){
    push(@arr, $item);
}
shuffle(@arr);
foreach $item(@arr){
    print "$item";
}

# Fisher–Yates shuffle
# for i from n−1 downto 1 do
#    j ← random integer such that 0 ≤ j ≤ i
#    exchange a[j] and a[i]

sub shuffle{
    $curr_index = @_ - 1;
    while($curr_index > 0){
    
        $rand_index = int(rand($curr_index + 1)); # $curr_index should also be included
        
        # exchange
        $temp = $_[$curr_index];
        $_[$curr_index] = $_[$rand_index];
        $_[$rand_index] = $temp;
        
        $curr_index--;
     }
}


        
