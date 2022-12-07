import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    i = 0


def generate_number():
    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)


def user_answer():
    user_result = prompt.string('Your answer: ')


def congratulations():
    if i == 3:
        print(f'Congratulations, {name}!')


def wrong_answer():
    print(f"'{user_result}' is wrong answer ;(. Correct answer was '{result}'.")
    print(f"Let's try again, {name}!")
