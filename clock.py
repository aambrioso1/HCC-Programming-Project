#!/usr/bin/env python

# ASCII Clock Project

# A project to display times using a classical seven-segment display of given 
# times input in a 24 hour format.

# The variable tm should be a string in the form of time on a 24 hour clock. 
# For example 01:17, 10:39, 20:41

# Note we assume the input 24-hour time strings are in the correct format.
   

def clock(tm):  # tm is a string representing a time in a 24-hour format.
    if tm == 'end': 
        return print('end')
    
    # We assign each digit to a variable.
    n1 = int(tm[0])
    n2 = int(tm[1])
    n3 = int(tm[3])
    n4 = int(tm[4])
    
    # We assign the different single lines of five characters each needed to build numbers and colon for the clock
    l ='+---+'    # line
    sd ='|   |'   # sides
    sp='+   +'    # side plusses
    d = '  o  '   # dot
    lp = '|    '  # left pipe
    rp = '    |'  # right pipe
    rpl = '    +' # right plus
    e = '     '   # empty
    
    # We define each of the numbers and the colon as lists of the line types.
    colon = [e,e,d,e,d,e,e]
    zero = [l, sd,sd,sp,sd, sd, l]
    one = [rpl, rp, rp, rpl, rp, rp, rpl]
    two = [l,rp, rp, l, lp, lp,l]
    three = [l,rp, rp, l, rp, rp,l]
    four = [sp, sd, sd, l, rp, rp, rpl]
    five = [l, lp,lp,l,rp,rp,l]
    six = [l, lp,lp,l,sd,sd,l]
    seven = [l, rp,rp,rpl,rp,rp,rpl]
    eight = [l, sd,sd,l,sd,sd,l]
    nine = [l, sd,sd,l,rp,rp,l]
    
    # chars is a list of the clock character definitions
    chars = [zero, one, two, three, four, five, six, seven, eight, nine]
    
    # We use a loop to write the four characters of the clock and the 
    # colon together one line at a time.
    for i in range(7):
        print(chars[n1][i],' ', chars[n2][i], colon[i], chars[n3][i],' ', chars[n4][i])
        
# We run the progam by iterating over a list of times.

# A list of times.        
tm_list = ['09:30','09:31','09:32','09:33', '09:34','09:35', 'end']

N = 38 # Used to count asterisks in print statements

# Print out clock face for all the times in the list.
"""
for i in tm_list: 
	clock(i)
	print(n * '*')
""" 
# Print out one face with the current time.
from datetime import datetime
right_now = datetime.now()
current_time = right_now.strftime('%H:%M')
# print(f'{current_time=}') # Prints out current time in the format '%H:%M'.


print(N * '*')
clock(current_time)
print(N * '*')


