#A program for deciding the type of solutions a quadratic equations has.
a=4
b=4
c=1
discriminant=b**2-4*a*c
if discriminant>0:
	print("The equations has two real solutions.")
if discriminant==0: #Note the use of == for a logical test.
	print("The equation has one real solution.")
if discriminant<0:
	print("The equation has two complex(non-real) solutions.")
	
