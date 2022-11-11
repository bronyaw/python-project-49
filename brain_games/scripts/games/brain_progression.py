#!/usr/bin/env python3
from random import randint
from brain_games.scripts import user_engine as user


def progr(x, y):  # makes list of progression of x ; y index = '..'
    string = []
    plus = x
    while len(string) != 10:
        string.append(plus)
        plus = plus + x
    string[y] = '..'
    return string


def main():
    name = user.welcome()
    print("What number is missing in the progression?")
    while user.cor_answers != 3:
        x = randint(1, 20)
        y = randint(1, 9)
        question = progr(x, y)
        answer = question[y - 1] + x
        user_answer = user.question_answer(' '.join(map(str, question)))
        user.choice(name, user_answer, str(answer))
    user.win(name)


if __name__ == '__main__':
    main()
