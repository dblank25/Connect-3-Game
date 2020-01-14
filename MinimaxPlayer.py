from Player import Player
import math
import time

CONNECT = 3
COLS = 4
ROWS = 3
EMPTY = ' '
TIE = 'TIE'

class MinimaxPlayer:
    def __init__(self, label):
        Player.__init__(self, label)
        self.board = None

    def move(self, state):
        start = time.time()
        maxval = -math.inf
        depth = 0
        for board in state.next(self.label):
            utility = self.minValue(board, depth)
            if utility > maxval:
                maxval = utility
                myboard = board
        end = time.time()
        print((end - start), " seconds per minimax player move")
        return myboard

    def utility(self, state, label, depth):  # returns utility value
        if label == 'O':
            goodness = (self.threeinarow(state, label) * 100) + self.twoinarow(state, label) - depth ** 2
        elif label == 'TIE':
            goodness = 0
        else:
            goodness = -((self.threeinarow(state, label) * 10000) + self.twoinarow(state, label)) + depth ** 2
        return goodness

    def maxValue(self,state,depth): # returns utility value
        if state.winner():
            return self.utility(state, state.winner(),depth)
        v = -math.inf
        for s in state.next('O'):
            v = max(v, self.minValue(s, depth+1))
        return v

    def minValue(self, state, depth):
        if state.winner():
            return self.utility(state, state.winner(),depth)
        v = math.inf
        for s in state.next('X'):
            v = min(v, self.maxValue(s, depth+1))
        return v

    def threeinarow(self, state,mylabel): # returns count of two in a row
        count = 0
        inarow = 3
        for i in range(COLS):
            for j in range(ROWS):
                label = state.get(i, j)
                if label == mylabel:
                    if self._test(state, inarow, label, i, j, +1, 0) \
                            or self._test(state, inarow, label, i, j, 0, +1) \
                            or self._test(state, inarow, label, i, j, +1, +1) \
                            or self._test(state, inarow, label, i, j, -1, +1):
                        count+=1
        return count

    def twoinarow(self, state, mylabel): # returns count of two in a row
        count = 0
        inarow = 2
        for i in range(COLS):
            for j in range(ROWS):
                label = state.get(i, j)
                if label == mylabel:
                    if self._test(state, inarow, label, i, j, +1, 0) \
                            or self._test(state, inarow, label, i, j, 0, +1) \
                            or self._test(state, inarow, label, i, j, +1, +1) \
                            or self._test(state, inarow, label, i, j, -1, +1):
                        count+=1
        return count

    def _test(self, state, inarow, label, i, j, di, dj):
        for _ in range(inarow-1):
            i += di
            j += dj
            if self.get(state, i, j) != label:
                return False
        return True


    def get(self,state, i, j):
        return state.b[i][j] if i >= 0 and i < COLS and j >= 0 and j < ROWS else None


