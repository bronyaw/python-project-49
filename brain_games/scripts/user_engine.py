import prompt


cor_answers = 0  # counts wins


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")
    return name


def wrong(name, user_answer, answer):
    print(f"'{user_answer}' is wrong answer ;( "
          f"Correct answer was {answer}\n"
          f"Let's try again, {name}!")


def win(name):
    print(f'Congratulations, {name}!')


def correct():
    global cor_answers
    print('Correct!')
    cor_answers += 1


def question_answer(question):
    print('Question:', question)
    user_answer = input('Your answer: ')
    return user_answer