#!/usr/bin/env python3
from random import randint
from math import gcd
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")
    brain_gcd(name)


def brain_gcd(user):  # easy enough ¯\_(ツ)_/¯
    print("Find the greatest common divisor of given numbers.")
    cor_answers = 0
    while cor_answers != 3:
        x = randint(1, 100)
        y = randint(1, 100)
        answer = gcd(x, y)  # find greatest div number
        print(f'Question: {x} {y}')
        user_answer = input('Your answer: ')
        try:
            if int(user_answer) == answer:
                cor_answers += 1
                print('Correct!')
            else:
                print(f"'{user_answer}' is wrong answer ;( "
                      f"Correct answer was '{answer}'\n"
                      f"Let's try again, {user}!")
                return
        except ValueError:  # if not int, so it doesnt break program
            print(f"'{user_answer}' is wrong answer ;( "
                  f"Correct answer was '{answer}'\n"
                  f"Let's try again, {user}!")
            return
    print(f'Congratulations, {user}!')


if __name__ == '__main__':
    main()
