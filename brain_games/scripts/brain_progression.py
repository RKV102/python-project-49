import brain_games.cli
import brain_games.games.arithmetic_progression


def main():
    print('Welcome to the Brain Games!')
    user_name = brain_games.cli.welcome_user()
    brain_games.games.arithmetic_progression.game(user_name)


if __name__ == '__main__':
    main()
