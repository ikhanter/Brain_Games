AMOUNT_OF_GAMES = 3


import prompt
import brain_games.cli as cli


def check_answer(name, correct_answer: str):
    answer = prompt.string('Answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    print(f"""'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
    return False


def run_game(game_function, abstract):
    name = cli.welcome_user()
    print(abstract)
    for i in range(AMOUNT_OF_GAMES):
        game = game_function()
        print(f'Question: {game[0]}')
        if not check_answer(name, game[1]):
            return
    print(f'Congratulations, {name}!')
