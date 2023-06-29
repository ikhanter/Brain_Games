#!usr/bin/env python3
import random, brain_games.scripts.brain_games as brain_games
import brain_games.engine.engine as engine


def gcd_game():
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    if number1 > number2:
        number1, number2 = number2, number1
    for i in range(1, number1 + 1):
        if (number1 % i == 0) and (number2 % i == 0):
            result = i
    return (f'{number1} {number2}', str(result))

def main():
    name = brain_games.main()
    print('Find the greatest common divisor of given numbers.')
    engine.count_correct(name, gcd_game(), gcd_game(), gcd_game())


if __name__ == '__main__':
    main()