import prompt


def question(question):
    print('Question:', question)


def check_answer(name, correct_answer: str):
    answer = prompt.string('Answer:')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
        return False


def count_correct(name, game_function1, game_function2, game_function3):
    correct_answer = 0
    result = (game_function1, game_function2, game_function3)
    while correct_answer < 3:
        for game in result:
            question(game[0])
            if check_answer(name, game[1]):
                correct_answer += 1
            else:
                correct_answer = 0
                break
        if correct_answer == 0:
            break
    if correct_answer == 3:
        print(f'Congratulations, {name}!')
