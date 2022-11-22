import random
import prompt


def main():
    print(f'Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    i = 0

    while i < 3:
        number = random.randint(1, 20)

        print(f'Question: {number}')
        result = prompt.string('Your answer: ')

        if number % 2 == 0 and result == "yes":
            print("Correct!")
        elif number % 2 != 0 and result == "no":
            print("Correct!")
        elif number % 2 == 0 and result == "no":
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        elif number % 2 != 0 and result == "yes":
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print(f'Wrong input!')
            print(f"Let's try again, {name}!")
            break

        i += 1
        if i == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
