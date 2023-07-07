#!usr/bin/env python3
import brain_games.engine as engine
import brain_games.games.brain_progression as progression_game


def main():
    engine.run_game(
        progression_game.generate_question_answer,
        progression_game.DESCRIPTION)


if __name__ == '__main__':
    main()
