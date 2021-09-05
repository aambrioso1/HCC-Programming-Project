# guess.py

# A simple guessing game.  
# The user picks a number between 1 and 10 inclusive.  
# The program tries to guess the number.   
# After each guess the user responds whether the guess 
# was too high (H), too low (L), or correct (C). 

guess = 5
min = 1
max = 11
keep_playing = True
input('Pick a number between 1 and 10 and hit enter.\n')
while(keep_playing):
    print(f'My guess is {guess}.\n')
    response = input('Input H or L or C.\n')
    if response == 'H':
        max = guess # set current guess as max
        guess = int((min + guess)/2)
    if response == 'L':
        min = guess # set current guess as min
        guess = int((max + guess)/2)
    if response == 'C':
        keep_playing = False

print(f'Your number was {guess}.')

        
