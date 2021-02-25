"""
We discuss the itertools module of the Python standard library with an example.
For the example we will the permuation method to unscramble a word.


ToDo:
I would like to expand this to a list of scramble words and the solutions.
The code will try check all permutations of each scrambled word against a list of
words.   List should contain words with similar spelling and more word that the needed.

We also include a recursive definition of the factorial function and the best natural way to compute
factorial in Python.


The documentation for the itertools module can be found here:  https://docs.python.org/3/library/itertools.html

Here are some of the methods I have found useful in the past:

permutations():  compute the permutations of an iterable
product():  computes the cartesian product of input iterables
combinations():  computes the combinations of an iterable
combinations_with_replacement:  computes the combinations with replacement of an iterable
isslice(iterable, start, stop [, step]):  Make an iterator that returns selected elements from the iterable.
tee():  return n independent iterators from a single iterable.

One other interesting thing about this module is that the documentation shows code roughly equivalent to the code used
to implement the functions.   This offers an opportunity to see how to implement some complex functionality
in Python.    I heard a well-known programmer say that studying the source code used in this library was like taking a g
graduate course on programming in Python.

"""

from itertools import permutations

string1 = 'word'
string2 = 'gritsn'

def fact(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n*fact(n-1)


list1 = permutations('gritsn', 3)		
list2 = permutations('gritsn')	

print(f'itertools.permutations(\'gritsn\', 3)	= {list1}')
print(f'itertools.permutations(\'gritsn\', 3)	= {list2}')

for i in list2: print(i)


"""
print(fact(5))

perm_list = []
for i, s in enumerate(permutations(string1,4),1):
	word = ''
	for c in s:
		word += c

	perm_list.append(word)

for i, w in enumerate(perm_list, 1):
	print(f'{i}. {w}')
"""