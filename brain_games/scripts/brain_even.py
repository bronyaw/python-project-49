#!/usr/bin/env python3
from random import randint
import prompt


def welcome_user():
    global name
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")


welcome_user()


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    cor_answers = 0
    while cor_answers != 3:
        question = randint(0, 100)
        print('Question:', question)
        user_answer = input('Your answer: ')
        if (question % 2) == 0:
            if user_answer == "yes":  # correct answer
                cor_answers += 1
                print('Correct!')
            else:  # wrong answer
                cor_answers = 0
                print(f"'{user_answer}'is wrong answer ;( "
                      f"Correct answer was 'no'\nLet's try again, {name}!")
        elif (question % 2) != 0:
            if user_answer == "no":  # correct answer
                cor_answers += 1
                print('Correct!')
            else:  # wrong answer
                cor_answers = 0
                print(f"'{user_answer}'is wrong answer ;( "
                      f"Correct answer was 'yes'\nLet's try again, {name}!")
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
