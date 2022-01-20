# pi_and_average_value_function

"""
A simple program that use the average value function to integrate a function.
Since the function in this is example integrates to 4arctan(1) the answer gives
approximation to Pi.

Using random sample to obtain numerical results is called the Monti Carlo Method.

See https://en.wikipedia.org/wiki/Monte_Carlo_method for more information
"""

import random as rd

num = 10000000 # number of iterations
sum = 0 # variable use to store value of sum


def f(x):
    return 4/(1 + x**2) 

for i in range(num):
    x = rd.random()
    sum += f(x) # increment sum by the value of our function
    
answer = sum/num # compute the average value.  Note the interval has length 1
print(f"\nThe value of pi is about {answer}\n") # Use an f-string to print the answer