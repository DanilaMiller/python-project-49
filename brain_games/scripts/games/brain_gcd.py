import random
import prompt
import math


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    i = 0

    while i < 3:
        number1 = random.randint(0, 50)
        number2 = random.randint(0, 50)
        real = math.gcd(number1, number2)
        print(f'Question: {number1} {number2}')
        result = prompt.string('Your answer: ')

        if int(result) == real:
            print("Correct!")
        else:
            print(f"'{result}' is wrong answer ;(. Correct answer was '{real}'.")
            print(f"Let's try again, {name}!")
            break

        i += 1
        if i == 3:
            print(f'Congratulations {name}!')


if __name__ == '__main__':
    main()
