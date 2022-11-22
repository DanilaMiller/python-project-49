import random
import prompt
from random import choice


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    i = 0

    while i < 3:
        random_number = random.randint(1, 10)
        list = [random.randint(1, 10)]
        b = 0

        while b < 10:
            number = list[b] + random_number
            list.append(number)
            b += 1
        result = choice(list)

        for j in range(len(list)):
            if list[j] == result:
                list[j] = '..'

        list_str = ' '.join(map(str, list))
        print(f'Question: {list_str}')
        result_by_user = prompt.string('Your answer: ')

        if int(result_by_user) == result:
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
