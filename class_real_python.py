"""
Follows:  https://realpython.com/python3-object-oriented-programming/

Although too advanced a topic for a beginning Python book, understanding dunder methods
 is an important part of mastering object-oriented programming in Python.
"""


kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

print(f'kirk: {kirk}')
print(f'kirk[1]: {kirk[1]}')
print(f'McCoy: {mccoy}')
print(f'McCoy[1]: {mccoy[1]}')


"""
From the online article.

"Classes are used to create user-defined data structures. Classes define functions called methods, 
which identify the behaviors and actions that an object created from the class can perform with its data."
"""

class Dog:
	# Class
    species = '\"Canis familiaris\"'

    def __init__(self, name, age):
        self.name = name + "dog"
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
(2) use
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

Alex = Dog('AlexDog', '14')
Sonya = Dog('SonyaDog', '7')


print(f'Alex.name: {Alex.name}')
print(f'Alex.age: {Alex.age}')
print(f'Alex.species: {Alex.species}')
print(f'Sonya.species: {Sonya.species}')
print(f'Sonya.age: {Sonya.age}')
print(Alex)
print(Sonya.speak('Ruff Ruff'))
