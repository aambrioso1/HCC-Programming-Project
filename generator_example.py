# generator_example.py
"""An example of a generator.   We create an iterator that generates 
the index of all the occurrence of a word in a text.  Rather than 
create a list to save the indices, we create a generator that will 
iterate through all of the indices.
There are several advantages:
(1)  Less memory is used.
(2)  The code is easier to read than it would be if we used a list and 
appended indices to it.

Interesting addition
Create shell command that would allow the user to provide the url.
"""
import requests

# text file from GP of Pride and Prejudice
url = "https://www.gutenberg.org/files/1342/1342-0.txt" 

response = requests.get(url)
if response.status_code == 404:
	raise SystemExit(f'HTTP response status: {res.status_code}') # Exit with message if URL is bad

START = 2440 # start of the book

book = response.text[START:] # book text starts at index 2440
my_word = 'the '

# define the generator just like a function except we use yield instead of return.
def index_of_word_iterator(text, word):
	for i, _ in enumerate(text):
		if text[i:i+len(word)].lower() == word:
			yield i

it = index_of_word_iterator(book, my_word) # create the iterator

# We use next() to generate the first three indices.
print(next(it))
print(next(it))
print(next(it))

indices = list(index_of_word_iterator(book, my_word)) # We use the iterator to generate a list
print(indices[:20]) # print the first 20 indices.

start_index = indices[0]
end_index = indices[0] + len(my_word)
print(f'The word located at {start_index} is "{book[start_index:end_index]}".') # We check the text at index 155
