from random import randint, choice


GAME_DESCRIPTION = 'What is the result of the expression?'


def game_run():
    x = randint(1, 20)
    y = randint(1, 20)
    question = choice([f'{x} + {y}',
                       f'{x} * {y}',
                       f'{x} - {y}'])
    answer = eval(question)
    return answer, question
