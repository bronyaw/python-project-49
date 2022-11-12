#!/usr/bin/env python3
from random import randint
from brain_games.scripts import user_engine as user


def progr(x):  # makes list of x progression
    string = []
    plus = x
    max_length = randint(6, 9)  # length of progression varies
    dot_index = randint(1, max_length - 1)
    while len(string) != max_length:
        string.append(plus)
        plus = plus + x
    string[dot_index] = '..'
    return string, dot_index


def main():
    user.welcome()
    user.game_announce('brain_progression')
    while True:
        x = randint(1, 20)
        question, dot_index = progr(x)
        answer = question[dot_index - 1] + x
        user.game_start(answer, ' '.join(map(str, question)))


if __name__ == '__main__':
    main()
