"""
The regular expressions operations (re) module is a standard Python
library.  It is a beautiful collection of operations for finding and manipulating 
matched text.  

This program use the re library to search the text in a file, regex.txt, for 
email addresses and phone numbers.  It copies
the emails and phone numbers it finds to a list called matches and prints 
them out neatly in a standard format.  You can avoid using a saved file as the text
source for the program.  The program has a string called text that 
is commented out (sort of) by using triple quotes  Remove the triple quotes and comment out the line that opens 
the regex.txt file.

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

I have some text here that can be used for demonstration purposes instead of 
reading a text file from the local current working directory.

text =  'This text file contains a few emails addresses and phone numbers.   
Alex phone is home number is 813-123-4567.
He has two email addresses aambrioso@hccfl.edu and alexambrioso@gmail.com.
Gregory has two phone nunbers:  (cell) (813) 685-1234 and work 253-7000 ext. 1234.
His email address in Greg.Johnson@yahoo.com.'

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
    
# Neatly prints out emails and phone numbers found 
# in the regex.txt file.
if len(matches) > 0:
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
