#!/usr/bin/env python3
from random import randint
from brain_games.scripts import user_engine as user


def is_prime(n):  # checks if number is prime
    for i in range(2, int(n / 2)):
        if (n % i) == 0:
            return False
    return True


def main():
    user.welcome()
    user.game_announce('brain_prime')
    while True:
        x = randint(1, 100)
        question = x
        if is_prime(x):  # True goes first
            answer = 'yes'
            user.game_start(answer, question)
        else:
            answer = 'no'
            user.game_start(answer, question)


if __name__ == '__main__':
    main()
