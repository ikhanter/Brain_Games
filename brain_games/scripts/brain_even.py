#!usr/bin/env python3
import random, prompt, brain_games.scripts.brain_games as brain_games


def ask_number(name):
    number = random.randint(1, 99999)
    even = True if number % 2 == 0 else False
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    if (even and answer == 'yes') or (not even and answer == 'no'):
        print('Correct!')
        return True
    else:
        print(f"""'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
        return False

def main():
    name = brain_games.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        if ask_number(name):
            correct_answers += 1
        else:
            correct_answers = 0
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()