#!usr/bin/env python3
import brain_main
import random
from random import choice


def main():
    brain_main.welcome_user()
    print('What number is missing in the progression?')
    i = 0

    while i < 3:
        brain_main.generate_number()
        list = [random.randint(1, 10)]
        b = 0

        while b < 10:
            number = list[b] + brain_main.random_number1
            list.append(number)
            b += 1
        result = choice(list)

        for j in range(len(list)):
            if list[j] == result:
                list[j] = '..'

        list_str = ' '.join(map(str, list))
        print(f'Question: {list_str}')
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
