"""
Given to squares on a chess board returns True if the squares 
are the same color and False if they are not.
"""

# Use zip to create a dictionary
d = dict(zip('abcdefgh',range(8)))

def cell_matcher(cell1, cell2):

	x1, y1 = cell1
	x2, y2 = cell2
	y1 = int(y1)
	y2 = int(y2)
	x1 = d[x1]
	x2 = d[x2]

	if (x1 + y1) % 2 == (x2 + y2) % 2:
		return True
	return False

def answer(b):
	if b:
		return 'are'
	return "are not"

c1, c2 = 'a1', 'a2'

ans = answer(cell_matcher(c1,c2))

print(f'The cells {c1} and {c2} {ans} the same color.')

c1, c2 = 'a1', 'b2'

ans = answer(cell_matcher(c1,c2))

print(f'The cells {c1} and {c2} {ans} the same color.')