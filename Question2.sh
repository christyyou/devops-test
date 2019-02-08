# Name: Weiran You
# School: University of Waterloo
# Student ID: 20540650
# Bash Version:3.2.57 on MacOS
# Devops-test, Question 2
#
# This shell script first generates a list of 10 CPU consuming process in descending order,
# then it creates 10 subdirectories under the current directory -- dir1 to dir 10
# and creates files named "file1" to "file10" in each subdirectory. Inside each file, one line
# of the list of process are stored.




#!/bin/bash
# Define the number of directories and files to create
len=10
# Generates a list of 10 CPU consuming process in descending order, and assign it to an array
IFS=$'\n'
my_array=($(ps -Ao user,uid,comm,pid,pcpu,pmem,tty,state,time -r | head -n 11))
declare my_array
# Create directories and files, write process to the file.
for ((i=1;i<=len;i++)); do
        mkdir -p "dir${i}" && touch "dir${i}/file${i}.txt"
        echo "${my_array[${i}]}" | tr -s " " >> "dir${i}/file${i}.txt"
done
