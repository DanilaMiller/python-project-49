#!usr/bin/env python3
from random import choice
import brain_main


def main():
    brain_main.welcome_user()
    print('What is the result of the expression?')
    i = 0

    while i < 3:
        global result
        brain_main.generate_number()
        operator = choice(['+', '-', '*'])
        if operator == '+':
            result = brain_main.random_number1 + brain_main.random_number2
        elif operator == '-':
            result = brain_main.random_number1 - brain_main.random_number2
        elif operator == '*':
            result = brain_main.random_number1 * brain_main.random_number2
        
        print(f'Question: {brain_main.random_number1} {operator} {brain_main.random_number2}')

        brain_main.user_answer()
        if int(brain_main.user_result) == result:
            print("Correct!")
        else:
            brain_main.wrong_answer(result)
            break

        i += 1
        if i == 3:
            brain_main.congratulations()


if __name__ == '__main__':
    main()
