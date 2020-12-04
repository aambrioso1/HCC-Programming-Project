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
	
	def __str__(self):
		return f"I am an Order object with position equal to {self.position}."

"""
first = Order(1)
second = Order(2)

print(f'first == second is {first == second}')
print(f'first != second is {first != second}')
print(f'first  > second is {first  > second}')
print(f'first >= second is {first >= second}')
print(f'first  < second is {first  < second}')
print(f'first <= second is {first <= second}')
"""