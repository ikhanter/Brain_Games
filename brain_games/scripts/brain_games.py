#!usr/bin/env python3
import brain_games.scripts.cli as cli


def main():
    global name
    print('Welcome to the Brain Games!')
    cli.welcome_user()
    name = cli.name


if __name__ == '__main__':
    main()
