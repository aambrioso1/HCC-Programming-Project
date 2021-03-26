customers = {
'001': ['Alex', 100.00], 
'314': ['Sonya', 25.25], 
'174':['Erika', 30.51], 
'521': ['Anthony', 34.56],
'231': ['Joseph', 13.76]
}

print(f'keys = {customers.keys()}')
print(f'values = {customers.values()}')
print(f'The list for customer 231 is {customers["231"]}') # Note that we need to use double quotes inside the f-string

def spent(s):
	value = customers[s][1]
	return value


print(f"Joseph spent ${spent('231')}")

# simple average value function with positional arguments
def avg1(v1,v2,v3,v4):
	average = (v1 + v2 + v3 + v4) / 4
	return average

"""
This creates an error since there are too many positional arguments
print(f'average  = {avg1(10,20,30,40,50)}')
"""

# *args allows have a variable number of positional arguments.  
# Think of it a create a list of the arguments called args with a length of len(args)
def avg2(*args):
	sum = 0
	for item in args:
		sum += item
	return sum / len(args)

print(f'The average is {avg2(10,20,30,40,50,60)}')

# keyword arguments allow for default values.
# Keyword and positional arguments:  positional arguments come first or you will get an error.

def total_int(principal, rate=5):
	return (rate / 100) * principal

print(f'interest = {total_int(1000, 7)}')

print(f'interest = {total_int(1000)}')


# **kwargs allows for a variable number of keyword arguments.   
# Think of it as creating a dictionary called kwargs with keys 
# being the stings of the keyword names and the values being the value
# associate with each keyword
def function(*args, **kwargs):
	sum = 0
	for item in args:
		sum += item
	for item in kwargs.keys():
		sum += kwargs[item]
	return sum
	

# Our function will take any number of positional arguments and keyword arguments and return the sum of the numbers.
# Note that we are assuming the arguments can be added togeter

print(f'total = {function(10, 20, 30, 40, 50, a=60, b=70, c=80)}')








