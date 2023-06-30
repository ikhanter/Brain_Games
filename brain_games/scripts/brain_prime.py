#!usr/bin/env python3
import brain_games.scripts.brain_games as brain_games
import brain_games.engine.engine as engine
import brain_games.games.brain_prime as prime_game


def main():
    brain_games.main()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    engine.count_correct(
        brain_games.name,
        prime_game.prime_game(),
        prime_game.prime_game(),
        prime_game.prime_game())


if __name__ == '__main__':
    main()
