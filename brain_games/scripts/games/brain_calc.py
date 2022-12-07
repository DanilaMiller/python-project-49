#!usr/bin/env python3
from random import choice
import brain_games


def main():
    brain_games.welcome_user()
    print('What is the result of the expression?')
    i = 0

    while i < 3:
        global result
        brain_games.generate_number()
        operator = choice(['+', '-', '*'])
        if operator == '+':
            result = brain_games.random_number1 + brain_games.random_number2
        elif operator == '-':
            result = brain_games.random_number1 - brain_games.random_number2
        elif operator == '*':
            result = brain_games.random_number1 * brain_games.random_number2
        
        print(f'Question: {brain_games.random_number1} {operator} {brain_games.random_number2}')

        brain_games.user_answer()
        if int(brain_games.user_result) == result:
            print("Correct!")
        else:
            brain_games.wrong_answer(result)
            break

        i += 1
        if i == 3:
            brain_games.congratulations()


if __name__ == '__main__':
    main()
