import brain_games
import math


def main():
    brain_games.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    i = 0

    while i < 3:
        brain_games.generate_number()
        result = math.gcd(brain_games.random_number1, brain_games.random_number2)
        print(f'Question: {brain_games.random_number1} {brain_games.random_number2}')
        brain_games.user_answer()

        if int(brain_games.user_result) == result:
            print("Correct!")
        else:
            brain_games.wrong_anwer(result)
            break

        i += 1
        if i == 3:
            brain_games.congratulations()


if __name__ == '__main__':
    main()
