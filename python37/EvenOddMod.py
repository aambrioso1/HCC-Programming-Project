def repeat():
	done = raw_input("Are you done? n/y: ")
	if done == "y":
		print "Thank you for coming"
		exit()
	elif done == "n":
		print "Ok"
		evenfinder()
	else:
		print "START TAKING ME SERIOUS"
		repeat()
def evenfinder():
	usernum = raw_input("Enter a number to test: ")
	if usernum.isdigit():
		usernum = int(usernum)
	else:
		print usernum, "is not a valid number"
		evenfinder()
	spoils = int(usernum) % 2
	if spoils == 0:
		print "even"
	else:
		print "odd"
	repeat()
evenfinder()