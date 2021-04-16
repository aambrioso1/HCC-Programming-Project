"""
combine_files.py - combines text from several files onto one new file and stores that new file
new directory

This program is intend to illustrate the use of command line arguments.
Additionally it will include:
(1)  Code to make a directory on the local computer.
(2)  Code to read and write to files the local computer.

The program also provides a simple example of how a command line script can be used to
leverage Python to help get work done.
"""


# Let's start by writing code that will create a directory to put the new file into

# First we process the command line arguments and assign the variable names to each text file
# We will call them text_name1, text_name2, text_name3, ...

# The built in sys directory has facilities to process the command line arguments.
# Specifically sys.argv returns a list of all the command line arguments
# for example if we input the following command
# >python combine_files file1 file2 file3
# Then sys.argv = ['python', combine_files, file1, file2, file3]


# We will open the files, read them, and combine the text into a single string, new_text.
# We use sys.argv[2:] to take the slice of the list of command line arguments starting with the first
# text file name.

import sys

# print(f'sys.argv = {sys.argv}')
new_text = ''
for arg in sys.argv[1:]:
	with open(f'temp/{arg}.txt', 'r') as reader:
		new_text += reader.read() + '\n'

# Next we create a directory to put the new text into

# The built in os module has facilities to help manage the local computer.
# We use it here to make the new directory

import os
os.mkdir('combined_files')


# Finally we write the text to the new directory.
with open(f'combined_files/combined_text_files.txt', 'w') as writer:
    writer.write(new_text)


# Additional feature would be to optionally have the last argument in the command line
# be the new file name.   The option would be indicated with -n:
# for example:  
# > combine_files.py -n file1 file2 file3 file_name
# Would combine file1, file2, and file3 into a file called file name.
# Without -n the command would combine the four files into a new file.

# Finally can we add some error handling in case the text files don't exist or the directory already exists
# Below is an example that illustrates the idea.

"""
try:
    os.remove(myfile)
except OSError as e:  ## if failed, report it back to the user ##
    print (f'Error: {e.filename} - {e.strerror}')
"""

