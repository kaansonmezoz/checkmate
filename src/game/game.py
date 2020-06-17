from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.game.game_screen import GameScreen

class Game:
    def __init__(self, chess_board):
        self.__game_screen = GameScreen()
        self.__chess_board = chess_board
        self.__game_screen.update(self.__chess_board.white_pieces(), self.__chess_board.black_pieces())

    def start(self):        
        while True:
            chess_piece = self.__select_chess_piece()
            self.__display_possible_moves(chess_piece)
            destination = self.__select_destination(chess_piece)
            self.__move_chess_piece(chess_piece, destination)

    def __select_chess_piece(self):
        # valid bir tas secene kadar devam etmeli
        self.__game_screen.click()
        return
    
    def __display_possible_moves(self, chess_piece):
        return
    
    def __select_destination(self, chess_piece):
        ## burada secme islemi valid bir pozisyon secilene kadar devam etmeli
        self.__game_screen.click()
        return
    
    def __move_chess_piece(self, chess_piece, destination):
        return


# burada oyun icin gerekli diger dependecyler her sey yaratilmali
# suan her class kendi dependencysisini yaratiyor onu kaldırmak lazim
