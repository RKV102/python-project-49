import brain_games.cli
import brain_games.games.parity_check
from brain_games.shared.greeting import main as greeting


def main():
    greeting()
    user_name = brain_games.cli.welcome_user()
    brain_games.games.parity_check.game(user_name)


if __name__ == '__main__':
    main()
