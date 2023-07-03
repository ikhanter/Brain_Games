RANDOM_BOT = 1
RANDOM_TOP = 99
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


import random


def generate_question_answer():
    number1 = random.randint(RANDOM_BOT, RANDOM_TOP)
    number2 = random.randint(RANDOM_BOT, RANDOM_TOP)
    if number1 > number2:
        number1, number2 = number2, number1
    for i in range(1, number1 + 1):
        if (number1 % i == 0) and (number2 % i == 0):
            result = i
    return (f'{number1} {number2}', str(result))
