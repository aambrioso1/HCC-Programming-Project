"""
A script for make mulitple copies of a file.

This program is based on Chapter 10: Organizing files of 
Al Swiegart's nice book Automate the Boring Stuff 
You can find Automate the Boring Stuff here: https://automatetheboringstuff.com/
There is lots more information about organizing files in the book. 
"""


# import standard libraries
import shutil, os
from pathlib import Path

p = Path.cwd() # returns the path for the current working directory
print(f'The current working directory is {p}')

base_file = 'Item30.py' # The name of the file to be copied.

# We use a loop to copy the base file over and over from Item{a}.py to Item{b}.py
a = 31
b = 90
for i in range(a, b+1):
	new_file = f'Item{i}.py'
	shutil.copy(p/base_file, p/new_file)