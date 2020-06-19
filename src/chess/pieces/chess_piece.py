from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from abc import ABCMeta, abstractmethod


class ChessPiece(metaclass=ABCMeta):
    def __init__(self, piece_type, color, number, y, x):
        self.__piece_type = piece_type
        self.__color = color
        self.__number = number
        self.__x = x
        self.__y = y

    def get_id(self):
        return self.__color + "_" + self.__piece_type + "_" + self.__number

    def color(self):
        return self.__color

    def get_type(self):
        return self.__piece_type

    def x(self):
        return self.__x

    def y(self):
        return self.__y

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
    def bishop(piece_type, color, number, y, x):
        from src.chess.pieces.bishop import Bishop
        return Bishop(piece_type, color, number, y, x)

    @staticmethod
    def king(piece_type, color, number, y, x):
        from src.chess.pieces.king   import King
        return King(piece_type, color, number, y, x)

    @staticmethod
    def knight(piece_type, color, number, y, x):
        from src.chess.pieces.knight import Knight
        return Knight(piece_type, color, number, y, x)
    
    @staticmethod
    def pawn(piece_type, color, number, y, x):
        from src.chess.pieces.pawn   import Pawn
        return Pawn(piece_type, color, number, y, x)

    @staticmethod
    def queen(piece_type, color, number, y, x):
        from src.chess.pieces.queen  import Queen
        return Queen(piece_type, color, number, y, x)

    @staticmethod
    def rook(piece_type, color, number, y, x):
        from src.chess.pieces.rook   import Rook
        return Rook(piece_type, color, number, y, x)