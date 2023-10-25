
class Player():
    def __init__(self, letter):
        self.letter = letter 
    def get_move(self, game):
        pass
    def get_letter(self):
        return self.letter

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        square = None
        while not valid_square:
            try:
                square = int(input(self.letter + '\'s turn. Input move (0-9): '))
                if square  in game.available_moves():
                    valid_square = True
                    break;
                print("Pensando pz sano . Try again.")

            except valueError:
                print("numero pz amigo")

        return square
