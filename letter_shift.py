# Create a dictionary
cipher_text = 'abcdefghijklmnopqrstuvwxyz'
plain_text = 'cdefghijklmnopqrstuvwxyzab'
code_dict = dict(zip(cipher_text, plain_text))
print(f'Here is the dictionary we will use:\n{code_dict}')

puzzle = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr\
 amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb\
 rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq()\
 gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

# Decode the message
message = ''
for c in puzzle:
	if c in cipher_text: # c is in the alphabet so we decode it.
		message += code_dict[c]
	else:
		message += c # c is not in the alphabet so we leave it alone

print(f'\nThe decoded message is:\n{message}')