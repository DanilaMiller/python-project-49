#!usr/bin/env python3
import math
import random
from brain_games.scripts.game_starter import starter


def game():
    random_number1 = random.randint(1,10)
    random_number2 = random.randint(1,10)
    correct_answer = math.gcd(random_number1, random_number2)
    question = f'{random_number1} {random_number2}'
    return question, correct_answer


def main():
    condition = 'Find the greatest common divisor of given numbers.'
    starter(game, condition)


if __name__ == '__main__':
    main()
