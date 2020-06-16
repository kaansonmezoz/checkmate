from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from .player import Player

class Human(Player):
    def __init__(self, color):
        super().__init__(color)

    def select_chess_piece(self):
        ## Should gets the input from window
        return
    
    def select_destination(self):
        ## should gets the input from window
        return