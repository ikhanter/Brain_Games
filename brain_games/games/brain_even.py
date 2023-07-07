import random


RANDOM_BOT = 1
RANDOM_TOP = 99999
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    question = random.randint(RANDOM_BOT, RANDOM_TOP)
    answer = 'yes' if question % 2 == 0 else 'no'
    return (question, answer)
