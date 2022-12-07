import brain_games


def main():
    brain_games.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0

    while i < 3:
        brain_games.generate_number()
        d = 2
        while d * d <= brain_games.random_number1 and brain_games.random_number1 % d != 0:
            d += 1
        if d * d > brain_games.random_number1:
            result = 'yes'
        else:
            result = 'no'

        print(f'Question: {brain_games.random_number1}')
        brain_games.user_unswer()

        if brain_games.user_result == result:
            print("Correct!")
        else:
            brain_games.wrong_answer(result)
            break

        i += 1
        if i == 3:
            brain_games.congratulations()


if __name__ == '__main__':
    main()
