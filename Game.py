from Player import Player
from RandomPlayer import RandomPlayer
from MinimaxPlayer import MinimaxPlayer
from MinimaxAlphaBetaPlayer import MinimaxAlphaBetaPlayer

class Game:
    def __init__(self, board):
        self.b = board
        self.player1 = Player('X')
        self.player2 = Player('O')


    def randomGame(self):
        sequence = [] # game sequence of moves
        players = [RandomPlayer('X'), RandomPlayer('O')]
        index = 0
        sequence.append(self.b)

        while self.b.winner() is None:
            move = players[index].move(self.b)
            sequence.append(move)
            self.b = move
            index = (index + 1) % len(players) # cycle through players list

        print(self.b.winner() + " wins!") if self.b.winner() != "TIE" else print("TIE")
        return sequence

    def minimaxGame(self):
        sequence = []  # game sequence of moves
        players = [RandomPlayer('X'), MinimaxPlayer('O')]
        index = 0
        sequence.append(self.b)
        while self.b.winner() is None:
            move = players[index].move(self.b)
            sequence.append(move)
            self.b = move
            index = (index + 1) % len(players) # cycle through players list

        print(self.b.winner() + " wins!") if self.b.winner() != "TIE" else print("TIE")
        return sequence

    def alphabetaGame(self):
        sequence = []  # game sequence of moves
        players = [RandomPlayer('X'), MinimaxAlphaBetaPlayer('O')]
        index = 0
        sequence.append(self.b)
        while self.b.winner() is None:
            move = players[index].move(self.b)
            sequence.append(move)
            self.b = move
            index = (index + 1) % len(players) # cycle through players list

        print(self.b.winner() + " wins!") if self.b.winner() != "TIE" else print("TIE")
        return sequence
