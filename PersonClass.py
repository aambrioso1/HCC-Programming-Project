#  You can find a nice explanation of Python classes here:  https://realpython.com/python3-object-oriented-programming/
# In fact, I highly recommend Real Python as a great website for learning Python.


class Person:
  # Class attribute
  species = 'human'
  
 # Associates an instance of the class with a description 
  def __str__(self):
    return f'{self.name} is a {self.species}.'
     
  # instance attributes
  def __init__(self, name, age):
    self.name = name
    self.age = age
        
  # instance methods
  def greets(self, phrase):
    return f'{self.name} says, {phrase}.'
	
  def responds(self, phrase):
    return f'{self.name}, replies {phrase}.'

# Inheritance
class Woman(Person):
  gender = 'female'
  likes = 'shoes'
  
  def responds(self, phrase='get lost'):
    return super().responds(phrase)
  

class Man(Person):
  gender = 'male'
  likes = 'football'

  def greets(self, phrase='what\'s your sign'):
    return super().greets(phrase)

class Classroom():
  def __init__(self, person_list): #[ ('Alex', 23), ('Samantha', 21), ]
    self.person_list = [Person(item[0], item[1]) for item in person_list]



  
