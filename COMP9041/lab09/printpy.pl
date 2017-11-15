#!/usr/bin/perl -w

# Case 1 : contains '''
if ( $ARGV[0] =~ m/'''/){
    # print "Case 1 \n";
    print "print(r\"$ARGV[0]\")\n";
}
# Case 2 : general
else{
    # print "Case 2 \n";
    print "print(r'''$ARGV[0]''')\n";
}
# print "print(r'''$content''')\n";
