from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

#from . import Renderer
from src.game.game_screen import GameScreen

class Game:
    def __init__(self, chess_board):
        #self.__renderer = Renderer(pygame)        
        self.__game_screen = GameScreen()
        self.__chess_board = chess_board    

# burada oyun icin gerekli diger dependecyler her sey yaratilmali
# suan her class kendi dependencysisini yaratiyor onu kaldırmak lazim
