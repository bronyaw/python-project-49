#!/usr/bin/env python3
from random import randint
from brain_games.scripts import user_engine as user


def main():
    name = user.welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while user.cor_answers != 3:
        question = randint(0, 100)
        user_answer = user.question_answer(question)
        if (question % 2) == 0:  # even
            answer = "'yes'"
            if str.lower(user_answer) == "yes":  # correct answer yes
                user.correct()
            else:  # wrong answer no
                print(user_answer, '1')
                return user.wrong(name, user_answer, answer)
        else:  # odd
            answer = "'no'"
            if str.lower(user_answer) == "no":  # correct answer no
                user.correct()
            else:  # wrong answer yes
                return user.wrong(name, user_answer, answer)
    user.win(name)


if __name__ == '__main__':
    main()
