# Weekend is set True if its a weekend
# Vacation is set to True if is a vacation.

def set_alarm(weekend, vacation):
	if weekend and not vacation:
		return 9
	elif weekend and vacation:
		return 10
	elif vacation:
		return 10
	return 6

print(set_alarm(True, True))
print(set_alarm(True, False))
print(set_alarm(False, True))
print(set_alarm(False, False))

# 10 9 10 6