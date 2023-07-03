import random


OPERATIONS = ('*', '+', '-')
RANDOM_BOT = -99
RANDOM_TOP = 99
DESCRIPTION = 'What is the result of the expression?'


def generate_question_answer():
    char = random.choice(OPERATIONS)
    number1 = random.randint(RANDOM_BOT, RANDOM_TOP)
    number2 = random.randint(RANDOM_BOT, RANDOM_TOP)
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
