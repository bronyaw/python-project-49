from random import randint


GAME_DESCRIPTION = "What number is missing in the progression?"


def gen_progression():
    progr = []
    num = randint(1, 20)
    plus = num
    max_length = randint(6, 9)
    dot_index = randint(1, max_length - 1)
    while len(progr) != max_length:
        progr.append(plus)
        plus += num
    progr[dot_index] = '..'
    return progr, dot_index


def game_run():
    question, dot_index = gen_progression()
    answer = question[dot_index - 1] + question[0]
    return answer, ' '.join(map(str, question))
