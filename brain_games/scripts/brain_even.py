import brain_games.cli
import brain_games.parity_check


def main():
    print('Welcome to the Brain Games!')


if __name__ == '__main__':
    main()
    user_name = brain_games.cli.welcome_user()
    brain_games.parity_check.game(user_name)
