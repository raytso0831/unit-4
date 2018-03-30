#Ray Tso
#3/30/18
#multipy.py 

from random import randint
def complement():
    n = randint(1,4)
    if n == 1:
        print('Great Job!')
    elif n == 2:
        print('Good job!')
    elif n == 3:
        print("AWESOME")
    else:
        print("You're a genius")
    numcorrect = 0


numCorrect = 0
while numCorrect < 5:
    num1 = randint(5,12)
    num2 = randint(5,12)
    question = 'What is ' + str(num1) + 'x' + str(num2) + '? '
    answer = int(input(question))
    if num1*num2 == answer:
        print('Correct')
        numCorrect += 1
    else:
        print('WRONG! The real answer was', num1+num2)
complement()

