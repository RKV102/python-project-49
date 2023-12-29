#!/usr/bin/env python3
import brain_games.cli
from brain_games.shared.greeting import main as greeting


def main():
    greeting()
    brain_games.cli.welcome_user()


if __name__ == '__main__':
    main()
