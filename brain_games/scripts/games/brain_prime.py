import random
import prompt


def main():
    welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


    while i < 3:
        generate_number()
        d = 2
        while d * d <= random_number1 and random_number1 % d != 0:
            d += 1
        if d * d > random_number1:
            result = 'yes'
        else:
            result = 'no'

        print(f'Question: {random_number1}')
        user_unswer()

        if user_result == result:
            print("Correct!")
        else:
            wrong_answer()
            break

        i += 1
        congratulations(i)


if __name__ == '__main__':
    main()
