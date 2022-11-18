from random import randint


GAME_DESCRIPTION = 'Answer "yes" if given number is prime. '\
                   'Otherwise answer "no".'


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n / 2) + 1):
        if (n % i) == 0:
            return False
    return True


def game_run():
    x = randint(1, 100)
    question = x
    if is_prime(x):
        answer = 'yes'
        return answer, question
    else:
        answer = 'no'
        return answer, question
