#!usr/bin/env python3
import brain_main


def main():
    brain_main.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0

    while i < 3:
        brain_main.generate_number()
        print(f'Question: {brain_main.random_number1}')
        brain_main.user_answer()

        if brain_main.random_number1 % 2 == 0 and brain_main.user_result == "yes":
            print("Correct!")
        elif brain_main.random_number1 % 2 != 0 and brain_main.user_result == "no":
            print("Correct!")
        elif brain_main.random_number1 % 2 == 0 and brain_main.user_result == "no":
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {brain_main.name}!")
            break
        elif brain_main.random_number1 % 2 != 0 and brain_main.user_result == "yes":
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {brain_main.name}!")
            break
        else:
            print('Wrong input!')
            print(f"Let's try again, {brain_main.name}!")
            break

        i += 1
        if i == 3:
            brain_main.congratulations()


if __name__ == '__main__':
    main()
