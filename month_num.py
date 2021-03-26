months = {'jan':1, 'feb':2, 'mar':3}


def month_num(string):
	if string in months.keys():
		return months[string]
	else:
		return 'Can\'t find that month'


for s in ['jan', 'mar', 'dec']:
	print(month_num(s))


def play(temp, summer):
	if 60 <= temp <= 100 and summer:
		return True
	elif 60 <= temp <= 90 and not summer:
		return True
	else:
		return False

print(f'If its 100 in the summer then play is {play(100, True)}')
print(play(100, False))
print(play(50, False))
