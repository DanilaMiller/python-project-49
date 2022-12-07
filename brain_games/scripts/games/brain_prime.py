#!usr/bin/env python3
import brain_main


def main():
    brain_main.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0

    while i < 3:
        brain_main.generate_number()
        d = 2
        while d * d <= brain_main.random_number1 and brain_main.random_number1 % d != 0:
            d += 1
        if d * d > brain_main.random_number1:
            result = 'yes'
        else:
            result = 'no'

        print(f'Question: {brain_main.random_number1}')
        brain_main.user_unswer()

        if brain_main.user_result == result:
            print("Correct!")
        else:
            brain_main.wrong_answer(result)
            break

        i += 1
        if i == 3:
            brain_main.congratulations()


if __name__ == '__main__':
    main()
