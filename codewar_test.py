list1 = [1,2,3,4,5,6,7,8,9,10, -11, -12, -13, -14, -15]
count = 0
for num in list1:
	if num < 0:
		count += 1
print(f'The number of negative numbers is {count}')
	
