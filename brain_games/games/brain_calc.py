import random


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
