#!usr/bin/env python3
import brain_games.engine.engine as engine
import brain_games.games.brain_even as game_even


def main():
    engine.run_game(
        game_even.generate_question_answer,
        game_even.DESCRIPTION)


if __name__ == '__main__':
    main()
