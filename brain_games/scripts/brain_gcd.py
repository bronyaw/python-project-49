#!/usr/bin/env python3


from brain_games.user_engine import game_start
from brain_games.games import game_gcd


def main():
    game_start(game_gcd)


if __name__ == '__main__':
    main()
