import prompt
from sys import exit


cor_answers = 0  # counts correct answers
name = ''  # placeholder for user name


def welcome(game_description):  # greets user, announces game rules
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")
    print(game_description)


def question_answer(question):  # takes user input and returnes its answer
    print('Question:', question)
    user_answer = input('Your answer: ')
    return user_answer


def choice(user_answer, answer):  # checks user answer
    if user_answer.lower() == str(answer):
        correct()
    else:
        wrong(user_answer, f"'{answer}'")


def correct():
    global cor_answers
    print('Correct!')
    cor_answers += 1


def wrong(user_answer, answer):
    print(f"'{user_answer}' is wrong answer ;( "
          f"Correct answer was {answer}\n"
          f"Let's try again, {name}!")
    exit()


def win():
    print(f'Congratulations, {name}!')
    exit()


def game_start(module):  # main engine
    welcome(module.GAME_DESCRIPTION)
    while cor_answers != 3:
        answer, question = module.game()
        user_answer = question_answer(question)
        choice(user_answer, answer)
    win()
