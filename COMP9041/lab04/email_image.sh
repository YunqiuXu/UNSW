#!/bin/sh

for img in "$@"
do
    # let the user view the image
    display "$img" # double quote --> in case the filename contains space
    
    # input email address
    echo "Address to e-mail this image to?" 
    read address
    
    # input message
    echo "Message to accompany image?"
    read message
    
    # output the result
    echo "$img sent to $address"
    
    # send the email
    echo "$message" | mutt -e 'set copy=no' -a "$img" -- "$address"
   
done
    
