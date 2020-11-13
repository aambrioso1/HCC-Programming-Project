import random as rd

k = 4

answer_list = ['Yes', 'No', 'Uncertain', 'I give up', 'Are you kidding']
num = rd.randint(0,k)
answer = answer_list[num]

print(f'My answer now is {answer}!')
