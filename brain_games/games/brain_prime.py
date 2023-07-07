import random


RANDOM_BOT = 3
RANDOM_TOP = 999
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generate_question_answer():
    question = random.randint(RANDOM_BOT, RANDOM_TOP)
    answer = 'yes' if check_prime(question) else 'no'
    return (question, answer)
