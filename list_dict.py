list_of_lists = [['a','b','c'], ['d', 'e', 'f', 'g']]

my_dict = {}

for list in list_of_lists:
	# key, *value = list[0], list[1:]
	key, *value = list # Uses catch-all unpacking - *value will catch the rest of the items in the list
	fixed_key = key # Need code here to fix key.
	my_dict[fixed_key] = value


print(my_dict)

