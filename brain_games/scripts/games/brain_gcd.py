#!/usr/bin/env python3
from random import randint
from math import gcd
from brain_games.scripts import user_engine as user


def main():
    user.welcome()
    user.game_announce('brain_gcd')
    while True:
        x = randint(1, 100)
        y = randint(1, 100)
        answer = gcd(x, y)  # find greatest div number
        question = f'{x} {y}'
        user.game_start(answer, question)


if __name__ == '__main__':
    main()
