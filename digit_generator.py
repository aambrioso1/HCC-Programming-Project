import random as rd

s1 = f'****\n****\n****\n****'


ast = {0: ' ', 1: '*'}

def rn():
	return rd.randint(0,1)

def val():
	return ast[rn()]


#  i in range(10):
#	print(val())


def dgt():
	arr = [val() for i in range(16)]
	s3 = ''
	ct = 0
	for i in range(4):
		ind = 4 * ct
		s3 = s3 + f'{arr[ind]}{arr[ind + 1]}{arr[ind + 2]}{arr[ind + 3]}\n'
		ct += 1
	return s3




"""
{val()}{val()}{val()}{val()}\n \
{val()}{val()}{val()}{val()}\n \
{val()}{val()}{val()}{val()}\n'
"""



for _ in range(1000):
	print(dgt())

"""

*****
   *
    *
*****  
    *
    *
*****  
"""