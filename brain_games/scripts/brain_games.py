#!usr/bin/env python3
import brain_games.scripts.cli


def main():
    print('Welcome to the Brain Games!')
    name = brain_games.scripts.cli.welcome_user()
    return name


if __name__ == '__main__':
    main()
