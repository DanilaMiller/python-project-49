import random
import prompt
from random import choice


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    i = 0

    while i < 3:
        number1 = random.randint(0, 40)
        number2 = random.randint(0, 40)
        op = choice(['+', '-', '*'])
        if op == '+':
            sum = number1 + number2
        elif op == '-':
            sum = number1 - number2
        elif op == '*':
            sum = number1 * number2

        print(f'Question: {number1} {op} {number2}')
        result = prompt.string('Your answer: ')

        if int(result) == sum:
            print("Correct!")
        else:
            print(f"{result} is wrong answer ;(. Correct answer was '{sum}'.")
            print(f"Let's try again, {name}!")
            break

        i += 1
        if i == 3:
            print(f'Congratulations {name}!')


if __name__ == '__main__':
    main()
