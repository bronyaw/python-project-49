from random import randint


GAME_DESCRIPTION = 'What is the result of the expression?'


def game():
    x = randint(1, 20)  # x, y -  variables for expression
    y = randint(1, 20)
    index = randint(0, 2)  # index for answer, question
    answer = [x + y, x * y, x - y]  # calculates
    question = [str(x) + ' + ' + str(y),  # prints
                str(x) + ' * ' + str(y),
                str(x) + ' - ' + str(y)]
    return (str(answer[index]), question[index])
