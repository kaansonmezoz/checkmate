from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.chess.position import Position
from src.chess.pieces.chess_piece import ChessPiece

class ChessMove:
    def __init__(self, chess_piece: ChessPiece, destination: Position):
        self.__chess_piece = chess_piece
        self.__destination = destination
    
    def __init__(self, chess_piece: ChessPiece, destination_y, destination_x):
        self.__chess_piece = chess_piece
        self.__destination = Position(destination_x, destination_y)
    
    def chess_piece(self) -> ChessPiece:
        return self.__chess_piece
    
    def destination(self) -> Position:
        return self.__destination
    
    def x(self):
        return self.__destination.x()
    
    def y(self):
        return self.__destination.y()
