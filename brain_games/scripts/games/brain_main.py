import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    i = 0


def generate_number():
    random_number = random.randint(1, 10)
