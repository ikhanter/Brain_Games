import prompt
import brain_games.cli as cli


AMOUNT_OF_GAMES = 3


def check_answer(name, correct_answer: str):
    answer = prompt.string('Answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    print(f"""'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
    return False


def run_game(run_play_logic, abstract):
    name = cli.welcome_user()
    print(abstract)
    for i in range(AMOUNT_OF_GAMES):
        question, real_answer = run_play_logic()
        print(f'Question: {question}')
        if not check_answer(name, real_answer):
            return
    print(f'Congratulations, {name}!')
