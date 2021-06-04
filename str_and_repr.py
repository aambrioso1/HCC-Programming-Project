# str type and repr type
# A str returns is a human-readable version of an object.
# A repr returns the printable representation of the object.

x = 7
y = '7'

"""
print(x)
print(y)

print(f'{x!r}')
print(f'{y!r}')

class BadClass:
	def __init__(self, x, y):
		self.x = x
		self.y = y

my_bad_class = BadClass(7, '7')
print(f'{my_bad_class.x=}')
print(f'{my_bad_class.y=}')
print(my_bad_class)

class GoodClass:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return f'GoodClass({x!r}, {y!r})'

my_good_class = GoodClass(7, '7')

print(my_good_class)
"""
