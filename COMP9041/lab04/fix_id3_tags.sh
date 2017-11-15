#!/bin/sh

# Version 1 can not handle some cases
# we can not cut by '-', some music will be wrong
# music/Triple J Hottest 100, 2006/10 - 19-20-20 - The Grates.mp3
# music/Triple J Hottest 100, 2012/3 - Breezeblocks - Alt-J.mp3
# Solution --> replace ' - ' by '%'


# question : Handling the few MP3 files correctly where using cut doesn't work will be considered a challenge exercise.
# What's the meaning of this

for folder in "$@"
do
    find "$folder" -type f | while read curr_music
    do
        title=`id3 -l "$curr_music" | head -n 1 | sed 's/ - /%/g' | cut -d'%' -f2`
        track=`id3 -l "$curr_music" | head -n 1 | sed 's/ - /%/g' | cut -d'%' -f1 | cut -d'/' -f3`
        artest=`id3 -l "$curr_music" | head -n 1 | sed 's/ - /%/g' | cut -d'%' -f3 | sed 's/.mp3:$//g'`
        album=`id3 -l "$curr_music" | head -n 1 | sed 's/ - /%/g' | cut -d'%' -f1 | cut -d'/' -f2`
        year=`echo $album | cut -d',' -f2 | sed 's/ //g'`
    
        # echo "$title"
        # echo "$artest"
        # echo "$album"
        # echo "$year"
        
        command1=`id3 -t "$title" "$curr_music"`
        command2=`id3 -T "$track" "$curr_music"`
        command3=`id3 -a "$artest" "$curr_music"`
        command4=`id3 -A "$album" "$curr_music"`
        command5=`id3 -y "$year" "$curr_music"`
        
    done
done




