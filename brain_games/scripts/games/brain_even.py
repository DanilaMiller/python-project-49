#!usr/bin/env python3
import random
from brain_games.scripts.game_starter import starter


def game():
    random_number1 = random.randint(1,10)
    question = f'{random_number1}'

    if random_number1 % 2 == 0:
        correct_answer = 'yes'
    elif random_number1 % 2 != 0:
        correct_answer = 'no'
    return question, correct_answer


def main():
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    starter(game, condition)


if __name__ == '__main__':
    main()
