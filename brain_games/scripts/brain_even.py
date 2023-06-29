#!usr/bin/env python3
import random, brain_games.scripts.brain_games as brain_games
import brain_games.engine.engine as engine


def generate_number():
    number = random.randint(1, 99999)
    even = 'yes' if number % 2 == 0 else 'no'
    return (number, even)

def main():
    name = brain_games.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    engine.count_correct(name, generate_number(), generate_number(), generate_number())


if __name__ == '__main__':
    main()