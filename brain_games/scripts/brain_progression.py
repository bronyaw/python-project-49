#!/usr/bin/env python3


from brain_games.user_engine import game_start
from brain_games.games import game_progression


def main():
    game_start(game_progression)


if __name__ == '__main__':
    main()
