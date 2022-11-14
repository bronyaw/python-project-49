from random import randint


GAME_DESCRIPTION = "What number is missing in the progression?"


def progr(x):  # makes list of x progression
    string = []
    plus = x
    max_length = randint(6, 9)  # length of progression varies
    dot_index = randint(1, max_length - 1)
    while len(string) != max_length:
        string.append(plus)
        plus = plus + x
    string[dot_index] = '..'
    return string, dot_index  # returns '..' index aswell


def game():
    x = randint(1, 20)
    question, dot_index = progr(x)
    answer = question[dot_index - 1] + x
    return answer, ' '.join(map(str, question))
