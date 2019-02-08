# Name: Weiran You
# School: University of Waterloo
# Student ID: 20540650
# Python Version: 2.7.10
# Devops-test, Question 1

# The function randomly generate a string with 10 letters (both cases)
# followed by 3 digits. Then it reverses the generated string and write both 
# string to a file.

# Effect: open a file, write to it and close the file.



import string
import random

# Define 'CharLen' as # of letters to generate and stored in 'CharList'
#        'DigLen' as # of digits to generate and stored in 'DigList'
CharLen = 10
DigLen = 3
CharList = []
DigList = []
# Generate a list with 10 letters.
Char = string.ascii_letters
for i in range(CharLen):
    CharList.append(random.choice(Char))
# Generate a list with 3 digits.
Dig = string.digits
for j in range(DigLen):
    DigList.append(random.choice(Dig))
# Append the above two lists.
FinalList = CharList + DigList
# Open the file 'ResultFile.txt', write both the generated string and the 
# reversed string and close the file.
f = open('ResultFile.txt','w+')
f.write(''.join(FinalList) + '\n')
f.write(''.join(FinalList)[::-1])
f.close()
