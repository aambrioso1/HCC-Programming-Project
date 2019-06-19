“””
This program searches the text in a file for 
email addresses and phone numbers.  It copies
them to a list called matches and prints them 
them neatly amd in a standard format.
This a slight modification of a progtam found at https://automatetheboringstuff.com/chapter7/
See also the documentstion at Python.org for the re library (regular expressions operations) here https://docs.python.org/3/library/re.html#re.ASCII
"""

import re
import os
 
 # Create an email regex.
 
with open('regex.txt') as f1: text=f1.read()
 
"""
text = 'Here are two email addresses aambrioso1@gmail.com and Erika.Ambrioso@fit.edu and several phone numbers (813)841-7072 and 813-842-7079, 841-7095, and 123-4567 ext. 789'
"""

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
     @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)
    
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
       # This code refromats the phone nimber in a standard way
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)

for groups in emailRegex.findall(text):
       matches.append(groups[0])
    
# Neatly prints out emails and phone nimbers founs # in the regex.txt file.
if len(matches) > 0:
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
