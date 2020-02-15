"""
A Python Lesson by Alex Ambrioso (2019)
This lesson has is about manipulating strings, lists, and reading and writing to files.
"""

import random as rd # A library for generating random numbers.
import os # A library for working with different operating systems we use it 
# to read and write to our hard-drive.

# We create three variables and set their values to three different strings.


article = 'a'
adjective ='fluffy'
noun = 'dog'


#  rn1 = rd.randint(0,5)
# rn2 = rd.randint(0,5)

# adjlist = ['nice', 'mean', 'small', 'red', 'fluffy', 'scappy']
# nounlist = ['boy', 'girl', 'man', 'woman', 'dog', 'cat']

"""
We set the variable sentence to an f-string.   This is a formated string and is new to Python 3.6 and 3.7.
It allows the programmer to format text in a simple way by putting placeholders, # {}, into text.  
"""

# Once you understand the program as is remark out sentence below and take the hash mark
# away from the second version of sentence.   Also remark out adjective,
# and noun and take out the hash marks in the next four lines.
#  What will the program do once you do this?

sentence = f"Once upon a time there was {article} {adjective} {noun}."
# sentence = f"Once upon a time there was {article} {adjlist[rn1]} {nounlist[rn2]}."

print(sentence)

# Now we will write and read text to and from files.

# We will check what the current working directory(cwd) and
# print out its contents.


# We check the current working directory (cwd) soe we know what directory the
# system is using for our IDE.  Then we create a path variable for that directory so
# we can write and read to and from it.

""" 
These three quotes and the three below will turn everything in between to a string
so the interpreter will ignore it.   
Once you understand the program above, read through the rest.   
Then take out the 6 quotes and this remark and run the program again.  

path = os.getcwd()

content = os.listdir(path)
print(f"The current working directory is {path}")
print(f"The contents of the working directory is: {content}\n")


# We save the sentence we created to a file called opening.txt
with open('MySentence.txt', 'w') as f1:  #Try 'a' for append
    f1.write(sentence)
    
# We open the file we created and print it out to make sure we saved
# it properly.
    
with open('MySentence.txt') as f2:
    MyFile = f2.read()
    
print(f"The text saved is: {MyFile}")
"""
