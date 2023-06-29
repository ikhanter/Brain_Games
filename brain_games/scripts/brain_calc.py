#!usr/bin/env python3
import brain_games.scripts.brain_games as brain_games
import brain_games.engine.engine as engine
import brain_games.games.brain_calc as calc_game


def main():
    name = brain_games.main()
    print('What is the result of the expression?')
    engine.count_correct(
        name,
        calc_game.calc_game(),
        calc_game.calc_game(),
        calc_game.calc_game())


if __name__ == '__main__':
    main()
