from Player import Player
import random


class RandomPlayer:
    def __init__(self, label):
        Player.__init__(self, label)
        self.board = None

    def move(self, state):
        nextMoves = state.next(self.label)
        move = random.choice(nextMoves)
        return move