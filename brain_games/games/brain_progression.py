import random


RANDOM_NUM_BOT = -999
RANDOM_NUM_TOP = 999
RANDOM_STEP_BOT = -99
RANDOM_STEP_TOP = 99
AMOUNT_STEPS_BOT = 5
AMOUNT_STEPS_TOP = 10
DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(initial_number, step, length):
    progression = [initial_number]
    for i in range(length):
        progression.append(progression[-1] + step)
    return progression


def generate_question_answer():
    number = random.randint(RANDOM_NUM_BOT, RANDOM_NUM_TOP)
    step = random.randint(RANDOM_STEP_BOT, RANDOM_STEP_TOP)
    amount_steps = random.randint(AMOUNT_STEPS_BOT, AMOUNT_STEPS_TOP)
    progression = generate_progression(number, step, amount_steps)
    erase_index = random.randint(1, len(progression) - 1)
    erase_number = progression[erase_index]
    progression[erase_index] = '..'
    return (' '.join(str(x) for x in progression), str(erase_number))
