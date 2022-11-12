import prompt
from sys import exit


GAME_QUESTIONS = {
    'brain_calc': 'What is the result of the expression?',
    'brain_even': 'Answer "yes" if the number is even, otherwise answer "no".',
    'brain_gcd': 'Find the greatest common divisor of given numbers.',
    'brain_prime': 'Answer "yes" if given number is prime. '
                   'Otherwise answer "no".',
    'brain_progression': "What number is missing in the progression?"
}

cor_answers = 0  # counts correct answers
name = ''  # placeholder for user name


def welcome():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")


def game_announce(game):
    print(GAME_QUESTIONS[game])


def game_start(answer, question):
    if cor_answers != 3:
        user_answer = question_answer(question)
        choice(name, user_answer, answer)
    else:
        win(name)


def question_answer(question):
    print('Question:', question)
    user_answer = input('Your answer: ')
    return user_answer


def choice(name, user_answer, answer):
    if user_answer.lower() == str(answer):
        correct()
    else:
        wrong(name, user_answer, f"'{answer}'")


def correct():
    global cor_answers
    print('Correct!')
    cor_answers += 1


def wrong(name, user_answer, answer):
    print(f"'{user_answer}' is wrong answer ;( "
          f"Correct answer was {answer}\n"
          f"Let's try again, {name}!")
    exit()


def win(name):
    print(f'Congratulations, {name}!')
    exit()
