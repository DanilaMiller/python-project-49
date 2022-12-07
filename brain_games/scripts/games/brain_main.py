import prompt
import random


def welcome_user():
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def generate_number():
    global random_number1
    global random_number2
    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)


def user_answer():
    global user_result
    user_result = prompt.string('Your answer: ')
    return user_result


def congratulations():
    print(f'Congratulations, {name}!')


def wrong_answer(result):
    print(f"'{user_result}' is wrong answer ;(. Correct answer was '{result}'.")
    print(f"Let's try again, {name}!")
