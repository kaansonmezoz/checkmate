from abc     import ABCMeta, abstractmethod

from .bishop import Bishop
from .king   import King
from .knight import Knight
from .pawn   import Pawn
from .queen  import Queen
from .rook   import Rook

from ..chess_board import ChessBoard

class ChessPiece(metaclass=ABCMeta):
    def __init__(self, name, color, x, y):
        self._name = name
        self._color = color
        self._x = x
        self._y = y

    def get_id(self):
        return self._color + "_" + self._name

    @abstractmethod
    def can_move(self):
        ##TODO: should be implemented
        pass

    @abstractmethod
    def move(self):
        ##TODO: should be implemented
        pass
    
    @abstractmethod
    def possible_moves(self, chess_board: ChessBoard):
        ##TODO: should return all possible moves from its current position
        pass

    @staticmethod
    def bishop(name, color, x, y):
        return Bishop(name, color, x, y)

    @staticmethod
    def king(name, color, x, y):
        return King(name, color, x, y)

    @staticmethod
    def knight(name, color, x, y):
        return Knight(name, color, x, y)
    
    @staticmethod
    def pawn(name, color, x, y):
        return Pawn(name, color, x, y)

    @staticmethod
    def queen(name, color, x, y):
        return Queen(name, color, x, y)

    @staticmethod
    def rook(name, color, x, y):
        return Rook(name, color, x, y)