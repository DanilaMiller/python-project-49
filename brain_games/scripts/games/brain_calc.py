#!usr/bin/env python3
from random import choice
import random
from game_starter import starter


def game():
  random_number1 = random.randint(1,10)
  random_number2 = random.randint(1,10)
  operator = choice('+-*')
  question = f'{random_number1} {operator} {random_number2}'
  if operator == '+':
      correct_answer = random_number1 + random_number2
  elif operator == '-':
      correct_answer = random_number1 - random_number2
  elif operator == '*':
      correct_answer = random_number1 * random_number2
  return question, correct_answer


def main():
  condition = 'What is the result of the expression?'
  starter(game, condition)


if __name__ == '__main__':
  main()
  