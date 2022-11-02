import prompt


def welcome_user():
    global name
    name = prompt.string('May i have your name? ')
    print(f"Hello, {name}!")
