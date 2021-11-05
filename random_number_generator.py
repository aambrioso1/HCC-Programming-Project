# random_number_generator.py

# Generates a random number with large, text numbers

import random as rd

num = rd.randint(1,30)  
N = 15

def rand_gen(num):  # tm is a string representing a time in a 24-hour format.
    
    # We assign each digit to a variable.
    n1 = num//10
    n2 = num % 10
    
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
        print(f'*{chars[n1][i]}  {chars[n2][i]} *')
        
print(N * '*')
rand_gen(num)
print(N * '*')


