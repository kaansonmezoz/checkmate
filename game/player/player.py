from abc import ABCMeta, abstractmethod
from ..chess_move import ChessMove

class Player(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def select_chess_piece(self):        
        ## it should return x,y coordinate of chess piece or just piece
        pass
    
    @abstractmethod
    def select_destination(self):
        ## it should selects destination for the chosen chess piece
        pass

    def next_chess_move(self):
        chess_piece = self.select_chess_piece()
        x, y = self.select_destination()
        return ChessMove(chess_piece, x, y)