"""
The regular expressions operations (re) module is a standard Python
library.  It is beautiful collection of operations for find and manipulating 
matched text.  

This program use the re library to search the text in a file, regex.txt, for 
email addresses and phone numbers.  It copies
them to a list called matches and prints then them 
them neatly in a standard format.  The program has a string call text that 
is commented out.   If you would like to avoid using a saved file as the text
source for the program, remove the comments and comment out the line that opens 
the regex.txt file,

The program is a slight modification of a program found at 
https://automatetheboringstuff.com/chapter7/

See also the documentation at Python.org for the re library
(regular expression operations) here
 https://docs.python.org/3/library/re.html#re.ASCII

"""
import re
import os
 
 
with open('regex.txt') as f1: text=f1.read()
 
"""

I have some text that can be used for demonstration purposes instead of read
reading a text file from the local working directory.

text =  'This text file contains a few emails addresses and phone numbers.   
Alex phone is home number is 813-123-4567.
He has two email addresses aambrioso@hccfl.edu and alexambrioso@gmail.com.
Gregory has two phone nunbers:  (cell) (813) 685-1234 and work 253-7000 ext. 1234.
His email address in Greg.Johnson@yahoo.com. 'Here are two email addresses aambrioso1@gmail.com and Erika.Ambrioso@fit.edu and several phone numbers (813)841-7072 and 813-842-7079, 841-7095, and 123-4567 ext. 789'

"""

# Create a regex for matching emails.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
     @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)
    
# Create a regex for matching phone numbers and identify 
# the parts of a phone number.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)
    
# Any text in the file which has a typical email or phone number will be added to the list matches.
matches = []
for groups in phoneRegex.findall(text):
       # This code reformats the phone number in a standard way by using
       # the blocks identified when the number was matched to the regex.
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)
for groups in emailRegex.findall(text):
       matches.append(groups[0])
    
# Neatly prints out emails and phone numbers founds 
# in the regex.txt file.
if len(matches) > 0:
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
