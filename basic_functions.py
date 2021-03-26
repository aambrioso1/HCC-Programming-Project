customers = {
'1321': ['Alex', 100.00], 
'9876': ['Sonya', 25.25], 
'0374':['Erika', 30.51], 
'5621': ['Anthony', 34.56],
'2321': ['Joseph', 13.76],
}
print(customers)
names = []
spending = []
for key in customers.keys():
	name, spent = customers[key]
	print(name)
	names.append(name)
	spending.append(spent)

print(names, spending)

for i in range(len(names)):
	n, s = names[i], spending[i]
	print(f'{n} spent ${s}.')


