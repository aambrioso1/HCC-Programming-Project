"""
We define a function, mirror(string) that takes a string and turns it into a palindrome by reversing the string
and appending it to the original string.
For example

mirror('word') returns 'worddrow'
"""

def mirror(string):
	length = len(string) # computes the length of the string
	palindrome = string # initialize the palinstrome with the original string
	for i in range(1, length + 1): # begins a loop where i will go from 1 to length
		# Since length - i will count down, the next line will add the letter 
		# of string to palindrome backword one at a time.
		palindrome += string[length - i]
	return palindrome

# Now we use the function on a couple of strings.
# We use interpolated f strings to generate a nice format for the output.
# The backslash is so that the quotes will be printed rather than interpreted.
print(f"mirror('word') = {mirror('word')}")
print(f"mirror('Devan') = {mirror('Devan')}")


