print "Welcome to the number guesser, Please select the range."
attempt = 0
min = input("what min do you want: ")
max = input("what max do you want: ")
test = (max + min) / 2
attempt = attempt + 1
print "Is your number %s?" % test
print "Valid inputs are: r if its right, h if its higher, and l if its lower"
def answer(min, max, test, attempt):
	ans = raw_input("Enter input: ")
	if ans == "h":
		min = test
		guess(min, max, test, attempt, ans)
	elif ans == "l":
		max = test
		guess(min, max, test, attempt, ans)
	elif ans == "r":
		if attempt == 1:
			print "Really"
		elif attempt < 5:
			print "childs play"
		elif attempt < 10:
			print "easy"
		elif attempt < 15:
			print "Not to bad"
		elif attempt < 20:
			print "You made me work for it"
		else:
			print "Wow, That hurt"
		print "It took %s attempts" % attempt
		raw_input("Press enter to continue...")
		exit()
	elif ans == "d":
		print "DEBUG: min:", min,"max:", max, "test:", test, "attempt:", attempt
		answer(min, max, test, attempt)
	else:
		print "Wrong input!"
		answer(min, max, test, attempt)
def guess(min, max, test, attempt, ans):
	if ans == "h":
		unc = test
		test = (max + min) / 2
		if unc == test:
			test = test + 1
		attempt = attempt + 1
		print "Is your number %s?" % test
		answer(min, max, test, attempt)
	elif ans == "l":
		unc = test
		test = (max + min) / 2
		if unc == test:
			test = test - 1
		attempt = attempt + 1
		print "Is your number %s?" % test
		answer(min, max, test, attempt)
answer(min, max, test, attempt)