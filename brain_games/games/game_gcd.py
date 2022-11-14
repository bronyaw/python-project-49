from random import randint
from math import gcd


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def game():
    x = randint(1, 100)
    y = randint(1, 100)
    answer = gcd(x, y)  # find greatest div number
    question = f'{x} {y}'
    return answer, question
