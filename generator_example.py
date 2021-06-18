# generator_example.py
"""An example of a generator.   We create an iterator that generates the index of all the occurrence of a word in a text.
Rather than create a list to save the indices, we create a generator that will iterate through all of the indices.
There are several advantages:
(1)  Less memory is used.
(2)  The code is easier to read than it would be used a list and appended indices to it. [EP]
"""
import requests

url = "https://www.gutenberg.org/files/1342/1342-0.txt" # text file from GP of Pride and Prejudice

response = requests.get(url)
if response.status_code == 404:
	raise SystemExit(f'HTTP response status: {res.status_code}') # Exit with message if URL is bad

book = response.text[2440:] # book text starts at index 2440

# define the generator just like a function except we use yield instead of return.
def index_of_the_iterator(text):
	for i, _ in enumerate(text):
		if text[i:i+4].lower() == 'the ':
			yield i

it = index_of_the_iterator(book) # create the iterator

# We use next() to generate the first three indices.
print(next(it))
print(next(it))
print(next(it))

indices = list(index_of_the_iterator(book)) # We use the iterator to generate a list
print(indices[:20]) # print the first 20 indices.
print(f'The text at book[155:159] is "{book[155:159]}".') # We check the text at index 155



