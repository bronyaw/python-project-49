#!/usr/bin/env python3
from random import randint
from brain_games.scripts import user_engine as user


def main():
    user.welcome()
    user.game_announce('brain_even')
    while True:
        question = randint(0, 100)
        if (question % 2) == 0:  # even
            answer = 'yes'
            user.game_start(answer, question)
        else:  # odd
            answer = 'no'
            user.game_start(answer, question)


if __name__ == '__main__':
    main()
