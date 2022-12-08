#!usr/bin/env python3
from game_starter import starter
import random
from random import choice


def game():
    random_number1 = random.randint(1, 10)
    list = [random.randint(1, 10)]
    correct_answer = choice(list)
    b = 0

    while b < 10:
        number = list[b] + random_number1
        list.append(number)
        b += 1

    for j in range(len(list)):
        if list[j] == correct_answer:
            list[j] = '..'

    list_str = ' '.join(map(str, list))
    question = f'{list_str}'
    return question, correct_answer


def main():
    condition = 'What number is missing in the progression?'
    starter(game, condition)


if __name__ == '__main__':
    main()
