import brain_games.cli
import brain_games.calculator


def main():
    print('Welcome to the Brain Games!')
    user_name = brain_games.cli.welcome_user()
    brain_games.calculator.game(user_name)


if __name__ == '__main__':
    main()
