#!/usr/bin/env python3
from random import randint
from sys import exit
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")
    brain_progression(name)


def progr(x, y):
    string = []
    plus = x
    while len(string) != 10:
        string.append(plus)
        plus = plus + x
    string[y] = '..'
    return string


def brain_progression(user):
    print("What number is missing in the progression?")
    cor_answers = 0
    while cor_answers != 3:
        x = randint(1, 20)
        y = randint(1, 9)
        question = progr(x, y)  # makes list of progression of x ; y index ='..'
        answer = question[y - 1] + x
        print('Question:', *question, sep=" ")
        user_answer = input('Your answer: ')
        try:
            if int(user_answer) == answer:
                cor_answers += 1
                print('Correct!')
            else:
                exit(f"'{user_answer}' is wrong answer ;( "
                     f"Correct answer was '{answer}'\n"
                     f"Let's try again, {user}!")
        except ValueError:
            exit(f"'{user_answer}' is wrong answer ;( "
                 f"Correct answer was '{answer}'\n"
                 f"Let's try again, {user}!")
    print(f'Congratulations, {user}!')


if __name__ == '__main__':
    main()
