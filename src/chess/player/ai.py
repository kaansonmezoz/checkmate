from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from .player import Player

class Ai(Player):
    def __init__(self, color):
        super().__init__(color)
    
    def select_chess_piece(self):
        ##TODO: AI based selection should be added
        return
    
    def select_destination(self):
        ##TODO: AI based selection should be added
        return