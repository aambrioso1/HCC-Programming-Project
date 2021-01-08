"""
From Python docs 3.  Data Model:  https://docs.python.org/3.9/reference/datamodel.html#customization
3.3. Special method names
A class can implement certain operations that are invoked by special syntax (such as arithmetic operations or
subscripting and slicing) by defining methods with special names. This is Python’s approach to operator
overloading, allowing classes to define their own behavior with respect to language operators. For instance,
if a class defines a method named __getitem__(), and x is an instance of this class, then x[i] is roughly 
equivalent to type(x).__getitem__(x, i). Except where mentioned, attempts to execute an operation raise an 
exception when no appropriate method is defined (typically AttributeError or TypeError).

From 3.3.1 Basic Customization
object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)
These are the so-called “rich comparison” methods. The correspondence between operator symbols and method 
names is as follows: 
x<y calls x.__lt__(y), x<=y calls x.__le__(y), x==y calls x.__eq__(y), x!=y calls x.__ne__(y), 
x>y calls x.__gt__(y), and x>=y calls x.__ge__(y).


Some information on repr() and str()
A nice article by Arpit Agarwal published by GeeksforGeeks:
https://www.geeksforgeeks.org/str-vs-repr-in-python/


https://docs.python.org/3/reference/datamodel.html#object.__repr__
https://docs.python.org/3/reference/datamodel.html#object.__str__

__repr__:  Called by the repr() built-in function to compute the “official” string representation of an object.
__str__:   Called by str(object) and the built-in functions format() and print() to compute the “informal” 
or nicely printable string representation of an object.
"""

class Order:
	description = 'Ordering'
	
	def __init__(self, position):
		self.position = position
	
	def __gt__(self, other):
		value = self.position < other.position
		return value
	
	def __ge__(self, other):
		value = self.position <= other.position
		return value
	
	def __repr__(self):
		return f'<Order({self.position})>'
	
	def __str__(self):
		return f'\"Order({self.position})\"'
		



first = Order(1)
second = Order(2)
third = Order(3)
print('first = ', first, '(Uses str())')
print(f'{{first}} = {first} (Uses str()) ')
print(f'{{first!r}} = {first!r} (Use repr())')
print(f'{{second!r}} = {second!r} (Use repr())')
print(f'{{third!r}} = {third!r} (Use repr())')

print(f'first == second is {first == second}')
print(f'first != second is {first != second}')
print(f'first  > second is {first  > second}')
print(f'first >= second is {first >= second}')
print(f'first  < second is {first  < second}')
print(f'first <= second is {first <= second}')

#  We show that our new class has an order that is recognized by Python
#  The sort command works for our new class!
my_list = [third, first, second]
print(f'my_list: {my_list}')
one, two, three = my_list
# Here is the list in its original order.
print(f'Before sort:  first in list = {one}, second in list = {two}, and third in list = {three}')

# Now we sort the list
my_list.sort(reverse=True)

one, two, three = my_list
# Here is the list the ordered list.
print(f'After sort:  first in list = {one}, second in list = {two}, and third in list = {three}')

