import sys

passwordFile = open('SecretPasswordFile.txt')
secretPassword = str(passwordFile.read())
print(secretPassword)
print('Enter your password.\n')
typedPassword = input()
print(typedPassword == secr)
if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')
