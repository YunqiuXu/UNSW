# COMP9041 w2tut
# Author : Yunqiu Xu

# 1. What is your tutor''s name, e-mail, how long have they been at UNSW, what are they studying, what is 1 interesting thing about them?



# 2. What are your class mates''s names, what are they each studying, what is 1 interesting thing about each of them?



# 3. Are there marks for attending lectures, tutorials or labs?



# 4. What is an operating system? What operating systems are running in your tute room? What operating system do CSE lab computers run?


# 5.
# a. Write a regexp to match C preprocessor commands in a C program.
egrep "^#+" tut02test1.txt

# b. Write a regexp to match all the lines in a C program except preprocessor commands
egrep -v "^#" tut02test1.txt


# c. Write a regexp to find line in a C program with trailing white space - one or white space at the end of line
egrep "\s+$" tut02test1.txt

# d. Write a regexp to match the names Barry, Harry, Larry and Parry
egrep "[BHLP]arry" tut02test1.txt

# e. Write a regexp to match a string containing the word hello followed later by the word world
egrep "hello.*?world" tut02test1.txt

# f. Write regexp to match the word calendar and all mis-spellings with 'a' replaced 'e' or vice-versa
egrep "c[ae]l[ae]nd[ae]r" tut02test1.txt

# g. Write regexp to match a list of positive integers separated by commas, e.g. 2,4,8,16,32
'HARD'
[0-9][0-9]*(,[0-9][0-9]*) or [0-9]+(,[0-9]+)*

# h. Write regexp to match a C string whose last character is newline
egrep "\n$" tut02test1.txt 

# 6. Five reasons why this attempt to search a file for HTML paragraph and break tags may fail.

$ grep <p>|<br> /tmp/index.html
True version: egrep "(<[\s]*p>|<[\s]*br>)" tut02test1.txt

# 7. Give examples for regexp
a. Perl: Perl
b. Pe*r*l: Pl, Pel, Peeeeeeeel, Prl, Prrrrrrl, Peeeeeerrrrrrrrl
c. .: any char except \n
d. [1-9][0-9][0-9][0-9]: any xxxx except 0xxx
e. I (love|hate) programming in (Perl|Python) and (Java|C): I hate programming in Perl and C

# 8. This regular expression [0-9]*.[0-9]* is intended to match floating point numbers such as '42.5'. Is it appropriate?
No, float has limit of digit number
And * means zero or more
True version: "[1-9][0-9]*\.[0-9]+"

# 9. What does the command egrep -v . print and why?
It print all lines consist of only whitespaces
"-v" means inverse match
"." means all chars except \n

Another example: egrep -v "2,3,4" tut02test1.txt
Matches all lines without "2,3,4"

# 10. match 129.94.172.1 to 129.94.172.25
egrep "129\.94\.172\.([1-9]|1[0-9]|2[0-5])[^\d]" tut02test1.txt

# 11. Describe matched strings,then give POSIX regexp to match them
# a. between the 1st ":" and second ":"
POSIX: ":[^:]+:"

# b. positive real numbers at the start of a line
POSIX: "^[0-9]+(\.[0-9]*)?"

# c. Names as represented in this file containing details of tute/lab enrolments
[^|,]+, [^|]+


# d. Names as above, but without the trailing spaces
[^|,]+,( [^| ]+)+


# 12. marks information for a single subject
# a. Give calls to the sort filter to display the data
# i. in order on student number
sort -k1 -n tut02test3.txt
# -n means sort by digit 

# ii. in ascending order on mark
sort -k2 -n tut02test3.txt

# iii. in descending order on mark
sort -rk2 -n tut02test3.txt

# b. Write calls to the grep filter to select details of
# i. students who failed
grep -E 'FL' tut02test3.txt 

# ii. students who scored above 90
grep -E '9[0-9]|100' tut02test3.txt

# iii. students with even student numbers
grep -E '^[0-9]*[02468]' tut02test3.txt

# c. Write a pipeline to print
# i. the details for the top 10 students (ordered by mark)
sort -rk2 -n tut02test3.txt | sed -n -e '1,10p'
sort -rk2 -n tut02test3.txt | head -10

# ii. the details for the bottom 5 students (ordered by mark)
sort -k2 tut02test3.txt | sed -n -e '1,5p'
sort -k2 tut02test3.txt | head -5
sort -rk2 tut02test3.txt | tail -5
 
# d. Assuming that the command cut -d' ' -f 3 can extract just the grades (PS, etc.), write a pipeline to show how many people achieved each grade (i.e. the grade distribution). E.g. for the above data
cut -d' ' -f3 tut02test3.txt | sort | uniq -c

# 13. Enrolments
# a. Which tute is Hinry Ng enrolled in
grep -E 'Ng, Hinry' tut02test4.txt | cut -d'|' -f3

# b. How many different tutorials are there
cut -d'|' -f3 tut02test4.txt | sort | uniq | wc -l

# c. What is the number of students in each tute?
cut -d'|' -f3 tut02test4.txt | sort | uniq -c

# d. Are any students enrolled in multiple tutes
cut -d'|' -f'1-2' tut02test4.txt | sort | uniq -d


fuckfuckfuck





 




















 
