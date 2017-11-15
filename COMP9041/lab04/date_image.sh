#!/bin/sh

for img in "$@"
do
    text=`ls -l "$img" | tr -s ' ' | cut -d' ' -f6-8`
    
    # get modify timestamp
    lastmodify=`stat "$img" | egrep "Modify" | sed "s/Modify: //g"`
    
    convert -gravity south -pointsize 36 -draw "text 0,10 '$text'" "$img" "$img"
    
    # preserve modify time
    touch -d "$lastmodify" "$img"
done
