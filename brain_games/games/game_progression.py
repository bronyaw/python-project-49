from random import randint


GAME_DESCRIPTION = "What number is missing in the progression?"


def gen_progression():
    string = []
    rng_num = randint(1, 20)
    plus = rng_num
    max_length = randint(6, 9)
    dot_index = randint(1, max_length - 1)
    while len(string) != max_length:
        string.append(plus)
        plus += rng_num
    string[dot_index] = '..'
    return string, dot_index


def game_run():
    question, dot_index = gen_progression()
    answer = question[dot_index - 1] + question[0]
    return answer, ' '.join(map(str, question))
