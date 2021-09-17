# replace.py

# Demo of the replace string method

my_string = """‘At the thame time,’ said Sleary, ‘I mutht put in my word, Thquire, tho
that both thides of the banner may be equally theen.  If you like,
Thethilia, to be prentitht, you know the natur of the work and you know
your companionth.  Emma Gordon, in whothe lap you’re a lying at prethent,
would be a mother to you, and Joth’phine would be a thithter to you.  I
don’t pretend to be of the angel breed myself, and I don’t thay but what,
when you mith’d your tip, you’d find me cut up rough, and thwear an oath
or two at you.  But what I thay, Thquire, ith, that good tempered or bad
tempered, I never did a horthe a injury yet, no more than thwearing at
him went, and that I don’t expect I thall begin otherwithe at my time of
life, with a rider.  I never wath much of a Cackler, Thquire, and I have
thed my thay.’
"""

my_new_string = my_string.replace('the ', '*')
my_new_string = my_new_string.replace('s', 'th')
my_new_string = my_new_string.replace('th', 's')
my_new_string = my_new_string.replace('Th', 's')
my_new_string = my_new_string.replace('*', 'the ')


print(50*'*')
print(my_string)
print(50*'*')
print(my_new_string)