from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.game.game_screen import GameScreen
from src.player.player import Player

class Game:
    def __init__(self, chess_board, player_1: Player, player_2: Player):
        self.__validate_player_arg(player_1, 'player_1')
        self.__validate_player_arg(player_2, 'player_2')
        
        self.__game_screen = GameScreen()
        self.__chess_board = chess_board
        self.__game_screen.update(self.__chess_board.white_pieces(), self.__chess_board.black_pieces())
        self.__player_order = []
        
        if player_1.color() == 'white':
            self.__player_order.append(player_1)
            self.__player_order.append(player_2)
        else:
            self.__player_order.append(player_2)
            self.__player_order.append(player_1)

    def start(self):        
        while True: 
            ## buradaki logicler aslinda oyunculara yuklenmeli ai'da surec boyle islemeyecek mesela chess_board ve GameScreen verilmesi gerekecek gibi duruyor
            player = self.__player_order.pop(0)
            chess_piece = self.__select_chess_piece()
            self.__display_possible_moves(chess_piece)
            destination = self.__select_destination(chess_piece)
            self.__move_chess_piece(chess_piece, destination)
            self.__player_order.append(player)

    def __validate_player_arg(self, obj, arg_name):
        if not isinstance(obj, Player):
            raise TypeError(arg_name + ' should be an instance of Player !')

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
