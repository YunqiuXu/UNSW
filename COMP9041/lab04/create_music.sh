#!/bin/sh

# get the path of $1
sample_path=`pwd`
sample_path=`echo "$sample_path/$1"`

# check whether folder $2 exist
if [ ! -d "$2" ]
then 
    mkdir "$2"
fi

cd "$2"

# create folders in $2
wget -q -O- 'https://en.wikipedia.org/wiki/Triple_J_Hottest_100?action=raw' | egrep -v "All time" | egrep -o "Triple J Hottest 100, [0-9]{4}" | while read curr_folder
do

    if [ ! -d "$curr_folder" ]
    then 
        mkdir "$curr_folder"
    fi

    cd "$curr_folder"

    # get some information
    album="$curr_folder"
    year=`echo $album | cut -d',' -f2 | sed 's/ //g'`
    track=1

    # load the songs
    wget -q -O- 'https://en.wikipedia.org/wiki/Triple_J_Hottest_100?action=raw' | sed -n "/Triple J Hottest 100, $year/,/\*/p" | sed -n '3,12p' | while read curr_song
    do
        # get the the rest information:
        # replace " - " by "%" then cut, artest is -f1 and title is -f2
        # if there exist "|" in [], choose the second one: sed "s/\[\[/\n/g" | sed "s/^.*|//g" | sed ':a;N;s/\n/\[\[/;ba;'
        # then remove the "#[]\"
        # replace "/" by "-"
        # remove the spaces in head and tail
        artest=`echo "$curr_song" | sed "s/ – /%/g" | cut -d'%' -f1 | sed "s/\[\[/\n/g" | sed "s/^.*|//g" | sed ':a;N;s/\n/\[\[/;ba;' | tr -d "#[]\"" | tr "/" "-" | sed "s/^[ ]*//g" | sed "s/[ ]*$//g"`
        title=`echo "$curr_song" | sed "s/ – /%/g" | cut -d'%' -f2 | sed "s/\[\[/\n/g" | sed "s/^.*|//g" | sed ':a;N;s/\n/\[\[/;ba;' | tr -d "#[]\"" | tr "/" "-" | sed "s/^[ ]*//g" | sed "s/[ ]*$//g"`
        file_name=`echo "$track - $title - $artest.mp3"`

        # set current path
        curr_path=`pwd`
        curr_path=`echo "$curr_path/$file_name"`

        # create file
        cp "$sample_path" "$curr_path"

        # do not add id3 information --> leave it unfixed
        # command1=`id3 -t "$title" "$file_name"`
        # command2=`id3 -T "$track" "$file_name"`
        # command3=`id3 -a "$artest" "$file_name"`
        # command4=`id3 -A "$album" "$file_name"`
        # command5=`id3 -y "$year" "$file_name"`

        track=`expr $track + 1`

    done

    # when this folder is finished, quit to $2
    cd ..
done
