#!usr/bin/env python3
import random
import brain_games.scripts.brain_games as brain_games
import brain_games.engine.engine as engine


def prime_game():
    number = random.randint(1, 9999)
    prime = 'yes'
    for i in range(2, number):
        if number % i == 0:
            prime = 'no'
            break
    return (number, prime)


def main():
    name = brain_games.main()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    engine.count_correct(name, prime_game(), prime_game(), prime_game())


if __name__ == '__main__':
    main()
