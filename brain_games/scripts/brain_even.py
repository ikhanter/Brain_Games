#!usr/bin/env python3
import brain_games.scripts.brain_games as brain_games
import brain_games.engine.engine as engine
import brain_games.games.brain_even as game_even


def main():
    name = brain_games.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    engine.count_correct(
        name,
        game_even.generate_number(),
        game_even.generate_number(),
        game_even.generate_number())


if __name__ == '__main__':
    main()
