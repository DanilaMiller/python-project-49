import random
import prompt
import math


def main():
    welcome_user()
    print('Find the greatest common divisor of given numbers.')

    while i < 3:
        generate_number()
        result = math.gcd(number1, number2)
        print(f'Question: {random_number1} {random_number2}')
        user_unswer()

        if int(user_result) == result:
            print("Correct!")
        else:
            wrong_anwer()
            break

        i += 1
        congratulations(i)


if __name__ == '__main__':
    main()
