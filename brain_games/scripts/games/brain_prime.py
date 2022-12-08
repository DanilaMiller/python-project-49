#!usr/bin/env python3
import random
from brain_games.scripts.game_starter import starter


def game():
    random_number1 = random.randint(1, 10)
    question = f'{random_number1}'
    d = 2
    while d * d <= random_number1 and random_number1 % d != 0:
        d += 1
    if d * d > random_number1:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def main():
    condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    starter(game, condition)


if __name__ == '__main__':
    main()
