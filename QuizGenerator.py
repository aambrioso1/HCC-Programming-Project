"""
A quiz generator by Alex Ambrioso (2019)

This is my reworking of a clever program found in the nice online etext "Automate the Boring Stuff"  by Al Sweigart.  The program creates quizzes with questions and answers in random order, along with the answer key.  In the book the program was used create quizzes on states and their capitals.  I have generalized it so that it creates quizzes on any reasonable list of matched items.  To use my version you will need to create a text file called quizpairs.txt in the working directory.  This file should contain all the matching terms for the quizzes.  Every two lines of the file should contain a matched pair.   For example, if you would like to create quizzes on the states and their capitals, the file might start as follows:

Florida
Tallahassee
Georgia
Atlanta
New York
Albany

You should create at least ten matched pairs for your file.
Once you create this file in the appropriate directory, the working directory for your Python installation, you can run the program.  It will generate 5 random quizzes based on your matching pairs.  These quizzes and their answer keys will be saved as text files in your working directory.  You can create more or fewer quizzes by adjusting the variable num.
"""

"""
I thought it my be fun and practical to create quizzes on Python terms.  Here is a list of Python terms amd expressions that could be used to make such quizzes.   Cut and paste this list to the text file, quizpairs.txt, or create your own list.  Technically each line should end in a newline.  I am not sure if cut and paste will do this so keep that in mind if you use my list below.

list
[1,'a',7]
set
{1,'a',7}
boolean
False
string
'man'
dictionary
{Anthony:1, Erika:2, Joseph:3}
tuple
(1,'a',7)
int
-1
float
3.14
floor division
//
exponentiation
**

"""
# We use the random library to shuffle the questions.
import random

# We use the file quizpairs.txt to create a dictionary of matching items for the quizzes.
f1 = open('quizpairs.txt')
qlist=[] # A list used to store the first item of the quiz pairs.
alist=[] # A list used to store the second item of the quiz pairs.
pos = 0
for line in f1:
    if pos % 2 == 0: qlist.append(line.rstrip())
    else: alist.append(line.rstrip())
    pos += 1
terms=dict(zip(qlist,alist))

#  You should always close open files so that any resouces used by the file are freed up.
f1.close()


num = 5 #  The number of quizzes to be generated.
#  Generates the quiz files and answer keys.
for quizNum in range(num):
    # Create the quiz and answer key files.
    quizFile = open('termquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('termquiz_answers%s.txt' % (quizNum + 1), 'w')
    
    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 10) + 'Term Matching Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    
    # Shuffle the order of the terms.
    questions = list(terms.keys())
    random.shuffle(questions)

    # Loop through all pairs of terms, making a question for each.
    for questionNum in range(len(terms)):
        # Get right and wrong answers.
        correctAnswer = terms[questions[questionNum]]
        wrongAnswers = list(terms.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        
        # Write the question and the answer options to the quiz file.   The next line shows the format of the quiz questions.
        quizFile.write('%s. Which of the following best matches with %s?\n' % (questionNum + 1, questions[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        
        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()
