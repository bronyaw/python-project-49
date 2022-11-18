from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_run():
    question = randint(0, 100)
    if (question % 2) == 0:  # even
        answer = 'yes'
        return answer, question
    else:  # odd
        answer = 'no'
        return answer, question
