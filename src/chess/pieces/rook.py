from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.chess.pieces.chess_piece  import ChessPiece
from src.chess.chess_board import ChessBoard

class Rook(ChessPiece):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)
    
    def can_move(self):
        ##TODO: should be implemented
        return

    def move(self):
        ##TODO: should be implemented
        return

    def possible_moves(self, chess_board: ChessBoard):
        ##TODO: should return all possible moves from its current position
        return
