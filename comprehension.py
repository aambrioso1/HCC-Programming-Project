"""
Build a list in three ways:
    (1) Using a for loop.
    (2) Using a map function.
    (3) Using comprehension.
    
You can find a nice tutorial on comprehension here:
    https://realpython.com/list-comprehension-python/
The tutorial include a discussion on when to use 
comprehension.

Here are the forms of comprehension in Python suggested by the article:

(3) new_list = [expression for member in iterable]
(4) new_list = [expression for member in iterable (if conditional)]
(5) new_list = [expression (if conditional) for member in iterable]
(6) At the end, I generate a set and a dictionary using comprehension.

"""
# We will generate lists using this string.
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# (1) Construct a list using a loop.
list1 = []
for letter in alphabet:
    list1.append(letter)

# (2) Construct using the map function. 
list2 = list(map(lambda i: i, alphabet))
print('map =', list2)

# (3) Construct a list using comprehension.
list3 = [letter for letter in alphabet]

print('list1 = ', list1)
print('list1 = ', list2)
print('list2 = ', list3)

# Examples using conditionals along with comprehension.
# (4) new_list = [expression for member in iterable (if conditional)]
vowels = {i for i in alphabet if i in 'aeiou'}
print('The vowels are', vowels)

# (4) new_list = [expression for member in iterable (if conditional)]

consonants =  {i for i in alphabet if i not in 'aeiou'}
print('The consonants are', consonants)

# (5) new_list = [expression (if conditional) for member in iterable]
delete_vowels = [letter if letter not in 'aeiou' else '*' for letter in alphabet]
print('Letters with vowels marked', delete_vowels)

# (6) Create a dictionary using comprehension.
dict1 = {i: alphabet[i] for i in range(26)}
print('The last letter of the alphabet is', dict1[25])


