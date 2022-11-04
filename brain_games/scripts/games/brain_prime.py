#!/usr/bin/env python3
from random import randint
from sys import exit
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")
    brain_prime(name)


def is_prime(n):  # checks if number is prime
    for i in range(2, int(n / 2)):
        if (n % i) == 0:
            return False
    return True


def str2bool_yes(string):  # returns True if string = 'yes'
    return string.lower() in ("yes")


def str2bool_no(string):  # return False if string = 'no'
    return string.lower() in ("no")


def brain_prime(user):
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    cor_answers = 0
    while cor_answers != 3:
        x = randint(1, 100)
        print("Question:", x)
        user_answer = input("Your answer: ")
        if is_prime(x):  # True goes first
            if str2bool_yes(user_answer):  # yes = correct answer
                cor_answers += 1
                print('Correct!')
            else:
                exit(f"'{user_answer}' is wrong answer ;( "
                     f"Correct answer was 'yes'\n"
                     f"Let's try again, {user}!")
        else:
            if str2bool_no(user_answer):  # no = correct answer
                cor_answers += 1
                print('Correct!')
            else:
                exit(f"'{user_answer}' is wrong answer ;( "
                     f"Correct answer was 'no'\n"
                     f"Let's try again, {user}!")
    print(f'Congratulations, {user}!')


if __name__ == '__main__':
    main()
