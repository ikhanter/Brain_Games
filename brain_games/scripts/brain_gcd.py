#!usr/bin/env python3
import brain_games.scripts.brain_games as brain_games
import brain_games.engine.engine as engine
import brain_games.games.brain_gcd as gcd_game


def main():
    name = brain_games.main()
    print('Find the greatest common divisor of given numbers.')
    engine.count_correct(
        name,
        gcd_game.gcd_game(),
        gcd_game.gcd_game(),
        gcd_game.gcd_game())


if __name__ == '__main__':
    main()
