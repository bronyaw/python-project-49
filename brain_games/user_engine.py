import prompt
from sys import exit


def game_start(module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")
    print(module.GAME_DESCRIPTION)
    cor_answers = 0
    while cor_answers != 3:
        answer, question = module.game_run()
        print('Question:', question)
        user_answer = input('Your answer: ')
        if user_answer.lower() == str(answer):
            cor_answers += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;( "
                  f"Correct answer was {answer}\n"
                  f"Let's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')
    exit()
