#!/usr/bin/env python3
from random import randint
from brain_games.scripts import user_engine as user


def progr(x):  # makes list of progression of x ; dot_index = '..'
    string = []
    plus = x
    max_length = randint(6, 9)
    dot_index = randint(1, max_length - 1)
    while len(string) != max_length:
        string.append(plus)
        plus = plus + x
    string[dot_index] = '..'
    return string, dot_index


def main():
    name = user.welcome()
    print("What number is missing in the progression?")
    while user.cor_answers != 3:
        x = randint(1, 20)
        question, dot_index = progr(x)
        answer = question[dot_index - 1] + x
        user_answer = user.question_answer(' '.join(map(str, question)))
        user.choice(name, user_answer, str(answer))
    user.win(name)


if __name__ == '__main__':
    main()
