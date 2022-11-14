#!/usr/bin/env python3


from brain_games import user_engine
from brain_games.games import game_gcd


def main():
    user_engine.game_start(game_gcd)


if __name__ == '__main__':
    main()
