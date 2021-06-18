# generator_example.py
"""An example of a generator.   We create an iterator that generates the index of all the occurrence of a word in a text.
Rather than create a list to save the indices, we create a generator that will iterate through all of the indices.
There are several advantages:
(1)  Less memory is used.
(2)  The code is easier to read than it would be if we appended the indices to a list. [EP]
"""
import requests

url = "https://www.gutenberg.org/files/1342/1342-0.txt" # text file from GP of Pride and Prejudice

response = requests.get(url)
if response.status_code == 404:
	raise SystemExit(f'HTTP response status: {res.status_code}') # Exit with message if URL is bad


book = response.text[2440:] # book starts at index 2440

def index_of_the_iterator(text):
	for i, _ in enumerate(text):
		if text[i:i+4].lower() == 'the ':
			yield i

it = index_of_the_iterator(book)

print(next(it))
print(next(it))
print(next(it))

index = list(index_of_the_iterator(book))
print(index[:20])
print('\n***********************************')
print(book[155:170])




