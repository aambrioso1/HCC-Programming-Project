"""
Written by Ambrioso @ 2020

A program to count words in text and confirm Zipf's Law:
https://en.wikipedia.org/wiki/Zipf%27s_law
Nice Video about the law:  https://youtu.be/fCn8zs912OE
(Law and graph introduced from:  0 to 1:20 min)

Note the program using a module my_plot_module.py that must be in the working directory.
""" 
# Requests is an elegant and simple HTTP library for Python, built for human beings.
import requests as req
import re # Regular expression library.  Part of standard library.
import collections as col# Standard libary. High-performance container datatypes
import os # Standard library.  Operating system interfaces. 
import my_plot_module as my_plot # My module for plotting a line graph

# Use requests to collected text from various websites (mostly Gutenberg.org).
r1 = req.get('http://www.gutenberg.org/cache/epub/5/pg5.txt') # Constitution
r2 = req.get('http://www.gutenberg.org/cache/epub/105/pg105.txt') # Persuasion
r3 = req.get('http://www.gutenberg.org/cache/epub/105/pg105.txt')  # Moby Dick
# This code uses requests to store big.txt in txt.
r4 = req.get('https://norvig.com/big.txt')

# Make one long text file.  Note that we are slicing of the first character 
# text files.  The first character return by the requests is
# a backslash.   This causes an error when we write a file.   
txt = r1.text + r2.text[1:] + r3.text[1:] + r4.text[1:]

# Here we write text to the hard drive
path = os.getcwd() # Get the current working directory
path2 = path + '\\my_text.txt' # create a path for new file
file = open(path2,'w') # open a file to that we will write to.
text = file.write(str(r1.text)[1:])
file.close()

# Use a regular expression to define a function that finds words.
def words(text): return re.findall(r'\w+', text.lower())

words_in_text = words(txt)

# Count the words in the text and find the top NUM words using methods
# found in the collections library.

word_counts = col.Counter(words_in_text)

NUM = 100
# The most_common(NUM) methods finds the most common words in text.
word_count_pairs = col.Counter(word_counts).most_common(NUM)

# Print out top num workds
count_list = []
print(f'Top {NUM} words in our text.')
print(50 * '*')
for pair in word_count_pairs:
    word, count = pair
    count_list.append(count)
    print(f'"{word}" occurs {count} times')

# Plot the rank number against the count.
# This graph will illustrate Zipf's Law.

xlist = [i for i in range(NUM)]
ylist =  count_list

# Use my my_plot module with its one method to create the graph    
my_plot.plot(xlist,ylist)