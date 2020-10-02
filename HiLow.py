
# This is a Hi-Low game.  The player picks a number between 1 and 100.  The computer tries to guess the number

import math
hi = 1
low = 100

print("\nPick a number between 1 and 100.  I will attempt to guess your number?")
wait=input("Hit enter to continue")
guess = math.floor((low+hi)/2)
print("My guess is: ", guess)
print("\nIs my guess too high or too low?")