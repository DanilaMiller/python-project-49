import random
import prompt
from random import choice


def main():
    welcome_user()
    print('What number is missing in the progression?')

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
        user_answer()

        if int(user_result) == result:
            print("Correct!")
        else:
            wrong_answer()
            break

        i += 1
        congratulations(i)


if __name__ == '__main__':
    main()
