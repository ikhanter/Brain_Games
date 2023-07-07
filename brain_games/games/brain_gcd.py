import random


RANDOM_BOT = 1
RANDOM_TOP = 99
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def search_gcd(lowest_number, highest_number):
    for i in range(1, lowest_number + 1):
        if (lowest_number % i == 0) and (highest_number % i == 0):
            gcd = i
    return gcd


def generate_question_answer():
    number1 = random.randint(RANDOM_BOT, RANDOM_TOP)
    number2 = random.randint(RANDOM_BOT, RANDOM_TOP)
    if number1 > number2:
        number1, number2 = number2, number1
    result_gcd = search_gcd(number1, number2)
    return (f'{number1} {number2}', str(result_gcd))
