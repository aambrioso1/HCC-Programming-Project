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

new_list = [expression for member in iterable]
new_list = [expression for member in iterable (if conditional)]
new_list = [expression (if conditional) for member in iterable]

At the end, I generate a set and a dictionary using comprehension.

"""
# We will generate lists using this string.
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# (1) Construct a list using a loop
list1 = []
for letter in alphabet:
    list1.append(letter)

# (2) Construct using the map function 
list2 = list(map(lambda i: i, alphabet))
print('map =', list2)

list3 = [letter for letter in alphabet]

print('list1 = ', list1)
print('list1 = ', list2)
print('list2 = ', list3)

vowels = {i for i in alphabet+alphabet if i in 'aeiou'}
print(vowels)

dict1 = {i: alphabet[i] for i in range(26)}
print('The last letter of the alphabet is', dict1[25])


