#!usr/bin/env python3
import random, brain_games.scripts.brain_games as brain_games
import brain_games.engine.engine as engine


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

def main():
    name = brain_games.main()
    print('What number is missing in the progression?')
    engine.count_correct(name, progression_game(), progression_game(), progression_game())


if __name__ == '__main__':
    main()