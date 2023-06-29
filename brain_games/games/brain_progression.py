import random


def progression_game():
    number = random.randint(-999, 999)
    step = random.randint(-99, 99)
    amount_steps = random.randint(5, 10)
    progression = [number]
    for i in range(amount_steps):
        progression.append(progression[-1] + step)
    erase_index = random.randint(1, len(progression))
    erase_number = progression[erase_index]
    progression[erase_index] = '..'
    return (' '.join(str(x) for x in progression), str(erase_number))
