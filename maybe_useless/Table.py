from Game import *
import sys


class Table():
    def __init__(self, player_list, game=games['nlh']):
        self.player_list = player_list
        self.game = game
        self.button = 0


class Player():
    def __init__(self, name, seat=None):
        self.name = name
        self.seat = seat


def main():
    pass

if __name__ == '__main__':
    main()
