#!/usr/bin/env python3
from random import randint
from sys import exit
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")
    brain_even(name)


def brain_even(user):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    cor_answers = 0
    while cor_answers != 3:
        question = randint(0, 100)
        print('Question:', question)
        user_answer = input('Your answer: ')
        if (question % 2) == 0:  # even
            if user_answer == "yes":  # correct answer yes
                cor_answers += 1
                print('Correct!')
            else:  # wrong answer no
                exit(f"'{user_answer}' is wrong answer ;( "
                     f"Correct answer was 'yes'\n"
                     f"Let's try again, {user}!")
        elif (question % 2) != 0:  # odd
            if user_answer == "no":  # correct answer no
                cor_answers += 1
                print('Correct!')
            else:  # wrong answer yes
                exit(f"'{user_answer}' is wrong answer ;( "
                     f"Correct answer was 'no'\n"
                     f"Let's try again, {user}!")
    print(f'Congratulations, {user}!')


if __name__ == '__main__':
    main()
