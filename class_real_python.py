"""
This lesson on classes follows this URL:
https://realpython.com/python3-object-oriented-programming/

This lesson does not include inheritance as the article does; but it extends 
the exploration of dunder methods by implenenting a __repr__ method and an ordering. 

Quote from the article:
"Although too advanced a topic for a beginning Python book, understanding dunder methods 
is an important part of mastering object-oriented programming in Python."
"""

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

print(f'kirk: {kirk}')
print(f'kirk[1]: {kirk[1]}')
print(f'McCoy: {mccoy}')
print(f'McCoy[1]: {mccoy[1]}')

"""
From the online article from Real Python

"Classes are used to create user-defined data structures. Classes define functions called methods, 
which identify the behaviors and actions that an object created from the class can perform with its data."
"""

class Dog:
	# Class
    species = '\"Canis familiaris\"'

    def __init__(self, name, age):
        self.name = name
        self.age = age

"""
Try:  
(1) Create some instances with attributes.
(2) Type the instance  
(3) Access class and instance attributes with the dot operator.
"""
class Dog:
	# Class
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


"""
 Try: Access the instance methods with the dot operator
"""

"""
Dunder (double underline) methods:
(1)  __str__
(2) u
"""

class Dog:
	# Class
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"{self.name} is a dog"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks {sound}"

"""
Methods like .__init__() and .__str__() are called dunder methods because 
they begin and end with double underscores. There are many dunder methods 
that you can use to customize classes in Python. Although too advanced a topic
for a beginning Python book, understanding dunder methods is an important part
of mastering object-oriented programming in Python.
"""

class Dog:
    # Class
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks {sound}"

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"{self.name} is a dog"

    # We add an ordering so that instance of the Dog class are order  by age.
    def __gt__(self, other):
        value = self.age< other.age
        return value
    
    def __ge__(self, other):
        value = self.age <= other.age
        return value

# We create two instances of the Dog class
Alex = Dog('AlexDog', '14')
Sonya = Dog('SonyaDog', '7')

# We call the class attribute with the dot operator
print(f'Alex.species: {Alex.species}')
print(f'Sonya.species: {Sonya.species}')

#  We call the instance attributes with the dot operator
print(f'Alex.name: {Alex.name}')
print(f'Alex.age: {Alex.age}')
print(f'Sonya.age: {Sonya.age}')

# A class method, speak, is invoked by the dot operator
print(Sonya.speak('Ruff Ruff'))
# Dunder methods

# The __str__ dunder method gives the class a nice output when you print the class instance
print(Alex)

# The __repr__ dunder method gives the object a nice output when the object is called
print(f'str(Alex) = {str(Alex)}')
print(f'repr(Alex) = {repr(Alex)}')

# If we start the REPL, we can import this module and create Alex as an instance of the Dog class.
# Then we can see this behavior:
# >>> Alex
# Alex is a dog
# >>> print(Alex)
# Alex is {Alex.age} years old

# Ordering
print(f'Is Alex > Sonya? {Alex > Sonya}')
print(f'Is Alex >= Sonya? {Alex >= Sonya}')
print(f'Is Alex < Sonya? {Alex < Sonya}')
print(f'Is Alex <= Sonya? {Alex <= Sonya}')
print(f'Is Alex == Sonya? {Alex == Sonya}')
print(f'Is Alex != Sonya? {Alex != Sonya}')