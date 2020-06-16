from .chess_board import ChessBoard
from .player.player import Player


class ChessGame():
    def __init__(self, player_1: Player, player_2: Player):
        self.__validate_player_arg(player_1, 'player_1')
        self.__validate_player_arg(player_2, 'player_2')
        
        self.__board = ChessBoard()
        self.__player_1 = player_1
        self.__player_2 = player_2
    
    def __validate_player_arg(self, obj, arg_name):
        if not isinstance(obj, Player):
            raise TypeError(arg_name + ' should be an instance of Player !')