import brain_games.cli
import brain_games.games.greatest_common_divisor
from brain_games.shared.greeting import main as greeting


def main():
    greeting()
    user_name = brain_games.cli.welcome_user() # CLI ничего не возвращает
    brain_games.games.greatest_common_divisor.game(user_name)


if __name__ == '__main__':
    main()
