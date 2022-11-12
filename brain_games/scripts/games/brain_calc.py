#!/usr/bin/env python3
from random import randint
from brain_games.scripts import user_engine as user


def main():
    user.welcome()
    user.game_announce('brain_calc')
    while True:
        x = randint(1, 20)  # x, y -  variables for expression
        y = randint(1, 20)
        index = randint(0, 2)  # index for answer, question
        answer = [x + y, x * y, x - y]  # calculates
        question = [str(x) + ' + ' + str(y),  # prints
                    str(x) + ' * ' + str(y),
                    str(x) + ' - ' + str(y)]
        user.game_start(str(answer[index]), question[index])


if __name__ == '__main__':
    main()
