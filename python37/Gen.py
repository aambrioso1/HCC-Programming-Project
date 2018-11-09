#Creates a list of m random numbers between 1 and n
Characters=["~","!","@","#","$","%","&","*"]
import random
m=3
n=7
myList=[random.randint(1,n) for i in range(m)]
PullList=[Characters[myList[i]] for i in range(3)]
print(PullList)