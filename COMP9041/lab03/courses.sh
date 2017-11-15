#!/bin/sh

# COMP9041 Lab02 Challenge Exercise: Scraping Courses

keyword=$1
keyword_head=`echo $1 | cut -c1`

ug_url="http://www.handbook.unsw.edu.au/vbook2017/brCoursesByAtoZ.jsp?StudyLevel=Undergraduate&descr="$keyword_head
pg_url="http://www.handbook.unsw.edu.au/vbook2017/brCoursesByAtoZ.jsp?StudyLevel=Postgraduate&descr="$keyword_head

wget -q -O- $ug_url $pg_url | egrep -o "$keyword.*?</A" | sed -E 's/.html">/ /g' | sed -E 's/...$//g' | sed -E 's/ $//g' | sort -k2 -n | uniq

# are we allowed to use 'egrep'?
