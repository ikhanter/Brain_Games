RANDOM_BOT = 3
RANDOM_TOP = 999
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


import random


def generate_question_answer():
    number = random.randint(RANDOM_BOT, RANDOM_TOP)
    prime = 'yes'
    for i in range(2, number):
        if number % i == 0:
            prime = 'no'
            break
    return (number, prime)
