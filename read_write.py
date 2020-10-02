import os

# Access the name of the current working directory and its contents
path = os.getcwd()
print('The current working directory and its contents are: ', path,os.listdir(path))

path2 = path + '\\my_text.txt'

file = open(path2,'a')
text = file.write('This is only a test!')
file.close()


file2 = open(path2,'r')
text2 = file2.read()
print('text', text2)

file2.close()