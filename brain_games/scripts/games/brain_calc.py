#!/usr/bin/env python3
from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")
    brain_calc(name)


def brain_calc(user):
    print('What is the result of the expression?')
    cor_answers = 0
    while cor_answers != 3:
        x = randint(1, 10)  # x, y -  variables for expression
        y = randint(1, 10)
        c = randint(0, 2)  # c - index for task, question_print
        task = [x + y, x * y, x - y]  # calculates
        question_print = [str(x) + '+' + str(y),  # prints
                          str(x) + '*' + str(y),
                          str(x) + '-' + str(y)]
        print('Question:', question_print[c])
        user_answer = input('Your answer: ')
        try:
            if int(user_answer) == task[c]:  # correct answer
                print('Correct!')
                cor_answers += 1
            else:  # wrong answer
                print(f"'{user_answer}' is wrong answer ;( "
                      f"Correct answer was '{task[c]}'\n"
                      f"Let's try again, {user}!")
                break
        except ValueError:  # if not int, so it doesnt break program
            cor_answers = 0
            print(task[c])
            print(f"'{user_answer}' is wrong answer ;( "
                  f"Correct answer was '{task[c]}'\n"
                  f"Let's try again, {user}!")
            break
        print(f'Congratulations, {user}!')


if __name__ == '__main__':
    main()
