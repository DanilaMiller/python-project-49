#!usr/bin/env python3
import brain_main
import math


def main():
    brain_main.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    i = 0

    while i < 3:
        brain_main.generate_number()
        result = math.gcd(brain_main.random_number1, brain_main.random_number2)
        print(f'Question: {brain_main.random_number1} {brain_main.random_number2}')
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
