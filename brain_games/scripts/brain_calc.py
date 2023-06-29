#!usr/bin/env python3
import random
import brain_games.scripts.brain_games as brain_games
import brain_games.engine.engine as engine


def calc_game():
    char = random.choice(['*', '+', '-'])
    number1 = random.randint(-99, 99)
    number2 = random.randint(-99, 99)
    match char:
        case '*':
            correct_str = f'{number1} * {number2}'
            correct_int = number1 * number2
        case '+':
            correct_str = f'{number1} + {number2}'
            correct_int = number1 + number2
        case '-':
            correct_str = f'{number1} - {number2}'
            correct_int = number1 - number2
    return (correct_str, str(correct_int))


def main():
    name = brain_games.main()
    print('What is the result of the expression?')
    engine.count_correct(name, calc_game(), calc_game(), calc_game())


if __name__ == '__main__':
    main()
