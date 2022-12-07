import brain_games


def main():
    brain_games.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0

    while i < 3:
        brain_games.generate_number()
        print(f'Question: {brain_games.random_number1}')
        brain_games.user_answer()

        if brain_games.random_number1 % 2 == 0 and brain_games.user_result == "yes":
            print("Correct!")
        elif brain_games.random_number1 % 2 != 0 and brain_games.user_result == "no":
            print("Correct!")
        elif brain_games.random_number1 % 2 == 0 and brain_games.user_result == "no":
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {brain_games.name}!")
            break
        elif brain_games.random_number1 % 2 != 0 and brain_games.user_result == "yes":
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {brain_games.name}!")
            break
        else:
            print('Wrong input!')
            print(f"Let's try again, {brain_games.name}!")
            break

        i += 1
        if i == 3:
            brain_games.congratulations()


if __name__ == '__main__':
    main()
