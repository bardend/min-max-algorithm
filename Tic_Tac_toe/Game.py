import math
import time
from Player import *

class Michi():
    def __init__(self):
        self.boar = self.make_boar()
        self.current_winer = False

    @staticmethod
    def make_boar():
        return  [' ' for i in range(9)]

    def print_boar(self):
        for row in [self.boar[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def print_boar_num(self):
        number = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number :
            print('| ' + ' | '.join(row) + ' |')

    def square_empty(self, square):
        return (self.boar[square] == ' ')

    def winner(self, square, letter):

        row_id = square//3
        row = self.boar[row_id*3 : (row_id+1)*3]

        if all([s == letter for s in row]):
            return True

        col_id = square %3
        col = [self.boar[col_id + i*3] for i in range(3)]

        if all([s == letter for s in col]):
            return True

        if square %2 == 0:
            dia1 = [self.boar[i] for i in [0, 4, 8]]
            if all([s == letter for s in dia1]):
                return True

            dia2 = [self.boar[i] for i in [2, 4, 6]]
            if all([s == letter for s in dia2]):
                return True
        
        return False

    def make_move(self, square, letter):
        self.boar[square] = letter 

    def available_moves(self):
        return [i for i,x in enumerate(self.boar) if x == ' ']

    def empty_squares(self):
        return ' ' in self.boar

def play(game, player1, player2, print_game = True):
    if print_game:
        game.print_boar_num()

    letter = 'X'
    win = 0

    while game.empty_squares():
        square = player1.get_move(game) if letter == '#' else player2.get_move(game)
        game.make_move(square, letter)
        print(square)

        if game.winner(square, letter):
            print(letter + ' wins!')
            win = 1
            game.print_boar()
            break

        game.print_boar()
        letter = '#' if letter == 'X' else 'X' # ^1 oponent
    
    if not win:
        print('It\s a tie!')


game = Michi()

player1 = HumanPlayer('#')
player2 = HumanPlayer('X')

play(game, player1, player2, print_game = True)
