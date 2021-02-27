"""
This program implements the Sieve of Erastosthenes in a straight forward way.
Here is a link to the Wikipedia page on about the Sieve:  https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

import math


k = 20 # The last number you want to check
list_of_numbers = [i for i in range(2,k+1)] # create the list starting with 2 so that one excluded

n = len(list_of_numbers) # we use the length of the list to help decide when to stop
primes = [] # We initial an empty list to put the primes in as we discover them
counter = 0 # We start a counter that will help use decided when to stop.
while(counter < math.sqrt(n)): # We repeat the process in the while loop until the counter reachings the square root
# of the length of the list.   With a little thought you can see that this is correct since.
# an number in the list with a prime factor greater that this will have one that is smaller.   
	counter += 1 # We increment the counter each time we go through the while loop.
	next_prime = list_of_numbers[0] # The first number on the list will always be prime.
	primes.append(next_prime) # We append this number to the list of primes.
	for i in list_of_numbers: # This loop removes all multiples of next prime from the list.
		if i % next_prime == 0:
			list_of_numbers.remove(i)

print(primes)
