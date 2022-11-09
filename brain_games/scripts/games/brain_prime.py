#!/usr/bin/env python3
from random import randint
from brain_games.scripts import user_engine as user


def is_prime(n):  # checks if number is prime
    for i in range(2, int(n / 2)):
        if (n % i) == 0:
            return False
    return True


def str2bool_yes(string):  # returns True if string = 'yes'
    return string.lower() in ("yes")


def str2bool_no(string):  # return False if string = 'no'
    return string.lower() in ("no")


def main():
    name = user.welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while user.cor_answers != 3:
        x = randint(1, 100)
        user_answer = user.question_answer(x)
        if is_prime(x):  # True goes first
            if str2bool_yes(user_answer):  # yes = correct answer
                user.correct()
            else:
                return user.wrong(name, user_answer, "'yes'")
        else:
            if str2bool_no(user_answer):  # no = correct answer
                user.correct()
            else:
                return user.wrong(name, user_answer, "'no'")
    user.win(name)


if __name__ == '__main__':
    main()
