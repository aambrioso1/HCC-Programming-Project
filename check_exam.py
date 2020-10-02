def check_exam(k_list, a_list):
	l = len(k_list)
	for i in range(l):
		print(f'k_list[{i}] = {k_list[i]}, a_list[{i}] = {a_list[i]}')

l1 = ['a', 'b']
l2 = ['a', 't']

check_exam(l1, l2)