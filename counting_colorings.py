"""
Counts the number of colorings possible if n walls are colored with n colors.  Also partitions the set of all colors by the number of colors used.
Uses itertools product function to comtrol the number of nested for loops.  The itertools library 
contains functions for creating iterators for efficient looping.
See:
https://docs.python.org/3/library/itertools.html#itertools.product
for detailed documentation.
"""

colors = ['a' ,'b','c','d', 'e', 'f', 'g', 'i', 'j', 'k', 'l']

n = 7
colorlist = []
colorcount = []
colorstring = ''

import itertools as it

for i in range(n):
    colorlist.append([]) # liss of colorings
    colorcount.append([]) # list of cardinality of colorings
    colorstring += colors[i] # String of the n colors

tuples = it.product(colorstring, repeat=n)
all = []
for i in tuples:
    newlist = list(i)
    all.append(newlist)
    for k in range(n):
       if len(set(newlist)) == k+1:
           colorlist[k].append(newlist)
        
"""
    if len(set(i)) == 5:
        quadlist.append(i)
    if len(set(i)) == 6:
        quadlist.append(i)
"""
# Compute the number of colorings by finding the length of each list.
for i in range(n):
    colorcount[i] = len(colorlist[i])


for i in range(n):
    print('\n********************************')
    print(f"The number of colorings using {i+1} color(s) is: {colorcount[i]}")
    print('**********************************')
print(f"\nTotal number of colorings: {len(all)}")
sum = 0
for i in range(n):
    sum +=colorcount[i]
print(f"Sum is {sum}")


"""
print('\n**********')
print('Monos')
print('**********')
print(colorlist[0])
print('\n**********')
print('Duos')
print('**********')
print(colorlist[1])
print('\n**********')
print('Trios')
print('**********')
print(colorlist[2])
print('\n**********')
print('Quads')
print('**********')
print(colorlist[3])
"""