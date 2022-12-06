import random
import prompt
penis

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0

    while i < 3:
        random_number = random.randint(1, 30)
        d = 2
        while d * d <= random_number and random_number % d != 0:
            d += 1
        if d * d > random_number:
            result = 'yes'
        else:
            result = 'no'

        print(f'Question: {random_number}')
        result_by_user = prompt.string('Your answer: ')

        if result_by_user == result:
            print("Correct!")
        else:
            print(f"'{result_by_user}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break

        i += 1
        if i == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
