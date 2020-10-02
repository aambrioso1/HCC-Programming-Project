#Slots by Alex Ambrioso 
#@Copyright 2017

#This program is an mimics a slot machine.
#It ask the user how many pulls she wishes to make 
#then generates that many list of 3 special characters.
#Typically and slot machine has n characters.  
#We use the following characters in this implementation

#Characters=["~","!","@","#","$","%","&","*"]

#We will implement the program as a series of functions

#Gen(n) generates a list of n random numbers
#Pick(list,) Picks  from a list of items
#Slots  uees Gen(n) and Pick(n) to create n lists of 3 special characters
#It as the user how many pulls of the slot machine he or she would like to make.
# then is prints out that number.

def Gen(n)
	import random
	for x in range(n):
	list[x]= random.randint(1,n)
	list
def Pick(List, ItemNumberList)
	for x in range len(ItemNumberList):
	PickList(x)=ItemNumberList(x)
	PickList
def Slots
	PullListNumbers=Gen(3)
	PickList=Pick(Characters,PullListNumbers)
	Print(PickList)
	