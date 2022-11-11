#!/usr/bin/env python3
from random import randint
from brain_games.scripts import user_engine as user


def main():
    name = user.welcome()
    print('What is the result of the expression?')
    while user.cor_answers != 3:
        x = randint(1, 20)  # x, y -  variables for expression
        y = randint(1, 20)
        index = randint(0, 2)  # index for answer, question
        answer = [x + y, x * y, x - y]  # calculates
        question = [str(x) + ' + ' + str(y),  # prints
                    str(x) + ' * ' + str(y),
                    str(x) + ' - ' + str(y)]
        user_answer = user.question_answer(question[index])
        user.choice(name, user_answer, str(answer[index]))
    user.win(name)


if __name__ == '__main__':
    main()
