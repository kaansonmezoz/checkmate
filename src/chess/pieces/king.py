from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.chess.pieces.chess_piece  import ChessPiece
from src.chess.chess_board import ChessBoard

class King(ChessPiece): # rok yapabilmesiyle ilgili bir state'i olmasi lazim. ayrica rok yaptigi zaman gerekli duzenlemelerin de yapilmasi gerekiyor. Boardda
    def __init__(self, piece_type, color, number, y, x):
        super().__init__(piece_type, color, number, y, x)
    
    def can_move(self):
        ##TODO: should be implemented
        return

    def move(self):
        ##TODO: should be implemented
        return

    def possible_moves(self, chess_board: ChessBoard):
        ##TODO: should return all possible moves from its current position
        return
