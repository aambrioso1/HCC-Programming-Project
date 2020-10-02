articles = ['A', 'The']
nouns = ['boy', 'girl', 'dog', 'tree']
verbs = ['plays', 'teases', 'grows', 'jumps']

for article in articles:
	for noun in nouns:
		for verb in verbs:
			print(f'{article} {noun} {verb}.')

