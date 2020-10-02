class Person:
  # Class attribute
  species = 'human'
  
  def __str__(self):
    return f"{self.name} is a {self}."
     
  # instance attributes
  def __init__(self, name, age):
    self.name = name
    self.age = age
        
  # instance methods
  def greets(self, phrase):
    return f'{self.name} says, {phrase}.'
	
  def responds(self, phrase):
    return f'{self.name}, replies {phrase}.'

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
