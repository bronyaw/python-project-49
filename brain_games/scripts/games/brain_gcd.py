#!/usr/bin/env python3
from random import randint
from math import gcd
from brain_games.scripts import user_engine as user


def main():
    name = user.welcome()
    print("Find the greatest common divisor of given numbers.")
    while user.cor_answers != 3:
        x = randint(1, 100)
        y = randint(1, 100)
        answer = gcd(x, y)  # find greatest div number
        user_answer = user.question_answer(f'{x} {y}')
        try:
            if int(user_answer) == answer:
                user.correct()
            else:
                return user.wrong(name, user_answer, answer)
        except ValueError:  # if not number, so it doesnt break
            return user.wrong(name, user_answer, answer)
    user.win(name)


if __name__ == '__main__':
    main()
