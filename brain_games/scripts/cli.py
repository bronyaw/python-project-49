import prompt


name = prompt.string('May i have your name? ')


def welcome_user():
    print(f"Hello, {name}!")
