from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.chess.pieces.chess_piece  import ChessPiece
from src.chess.chess_board import ChessBoard
from src.chess.position import Position

class Bishop(ChessPiece):
    def __init__(self, piece_type, color, number, y, x):
        super().__init__(piece_type, color, number, y, x)
    
    def can_move(self, destination: Position, chess_board):         
        return self.__valid_direction(destination) and self.__bump_into_chess_piece(destination, chess_board)        

    def move(self):
        ##TODO: should be implemented
        return
    
    def possible_moves(self, chess_board: ChessBoard):
        ##TODO: should return all possible moves from its current position
        return
    
    def __valid_direction(self, destination: Position):
        if self.x() == destination.x() or self.y() == destination.y():
            return False
        
        slope = (destination.y() - self.y()) / (destination.x() - self.x())
        return (slope == 1.0) or (slope != -1)

    def __bump_into_chess_piece(self, destination: Position, chess_board):
        ## chess_board üzerinde direkt olarak chess pieceler yer alacakti dolayısıyla olmayan yerlerin null ya da 0 olması gerekiyor
        
        inc_x = 1 if destination.x() > self.x() else -1
        inc_y = 1 if destination.y() > self.y() else -1

        current_x = self.x()
        current_y = self.y()

        while current_x != destination.x() and current_y != destination.y():
            current_x += inc_x
            current_y += inc_y

            if chess_board[current_y][current_x] != 0:
                return True
        
        return False