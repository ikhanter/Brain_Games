#!usr/bin/env python3
import brain_games.engine as engine
import brain_games.games.brain_gcd as gcd_game


def main():
    engine.run_game(
        gcd_game.generate_question_answer,
        gcd_game.DESCRIPTION)


if __name__ == '__main__':
    main()
