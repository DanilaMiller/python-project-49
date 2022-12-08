#!/usr/bin/env python3
import prompt


def is_it_correct(question, correct_answer, name):
  print(f'Question: {question}')
  user_answer = prompt.string('Your answer: ')

  if user_answer == str(correct_answer):
    print('Correct!')
    return True
  else:
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")
    return False


def starter(game, condition):
  print('Welcome to the Brain Games!')
  name = prompt.string('May I have your name? ')
  print(f'Hello, {name}!')
  print(condition)
  
  count_correct = 0
  count_wrong = 0
  while count_correct < 3 and count_wrong == 0:
    question, correct_answer = game()
    if is_it_correct(question, correct_answer, name) == True:
        count_correct += 1
    else:
        count_wrong += 1
    if count_correct == 3:
        print(f'Congratulations, {name}!')
