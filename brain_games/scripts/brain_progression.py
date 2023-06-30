#!usr/bin/env python3
import brain_games.scripts.brain_games as brain_games
import brain_games.engine.engine as engine
import brain_games.games.brain_progression as progression_game


def main():
    brain_games.main()
    print('What number is missing in the progression?')
    engine.count_correct(
        brain_games.name,
        progression_game.progression_game(),
        progression_game.progression_game(),
        progression_game.progression_game())


if __name__ == '__main__':
    main()
