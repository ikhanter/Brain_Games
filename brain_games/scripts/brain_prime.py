#!usr/bin/env python3
import brain_games.engine as engine
import brain_games.games.brain_prime as prime_game


def main():
    engine.run_game(
        prime_game.generate_question_answer,
        prime_game.DESCRIPTION)


if __name__ == '__main__':
    main()
