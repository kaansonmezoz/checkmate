from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from abc     import ABCMeta, abstractmethod








#from src.chess.chess_board import ChessBoard

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
    def possible_moves(self, chess_board):
        ##TODO: should return all possible moves from its current position
        pass

    @staticmethod
    def bishop(name, color, x, y):
        from src.chess.pieces.bishop import Bishop
        return Bishop(name, color, x, y)

    @staticmethod
    def king(name, color, x, y):
        from src.chess.pieces.king   import King
        return King(name, color, x, y)

    @staticmethod
    def knight(name, color, x, y):
        from src.chess.pieces.knight import Knight
        return Knight(name, color, x, y)
    
    @staticmethod
    def pawn(name, color, x, y):
        from src.chess.pieces.pawn   import Pawn
        return Pawn(name, color, x, y)

    @staticmethod
    def queen(name, color, x, y):
        from src.chess.pieces.queen  import Queen
        return Queen(name, color, x, y)

    @staticmethod
    def rook(name, color, x, y):
        from src.chess.pieces.rook   import Rook
        return Rook(name, color, x, y)