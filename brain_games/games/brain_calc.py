import random


OPERATIONS = ('*', '+', '-')
RANDOM_BOT = -99
RANDOM_TOP = 99
DESCRIPTION = 'What is the result of the expression?'


def calculate_answer(operation, number1, number2):
    match operation:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2


def generate_question_answer():
    operation = random.choice(OPERATIONS)
    number1 = random.randint(RANDOM_BOT, RANDOM_TOP)
    number2 = random.randint(RANDOM_BOT, RANDOM_TOP)
    formed_str_question = f'{number1} {operation} {number2}'
    calculated_answer = calculate_answer(operation, number1, number2)
    return (formed_str_question, str(calculated_answer))
