#!usr/bin/env python3
import brain_games.engine.engine as engine
import brain_games.games.brain_calc as calc_game


def main():
    engine.run_game(
        calc_game.generate_question_answer,
        calc_game.DESCRIPTION)


if __name__ == '__main__':
    main()
