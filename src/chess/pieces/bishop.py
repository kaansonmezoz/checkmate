from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.chess.pieces.chess_piece  import ChessPiece
from src.chess.chess_board import ChessBoard

class Bishop(ChessPiece):
    def __init__(self, piece_type, color, number, y, x):
        super().__init__(piece_type, color, number, y, x)
    
    def can_move(self, destination_y, destination_x, chess_board): 
        ##TODO: Destination hep bu sekilde ikililerle gelecek aslında bunu bir classa cikmak daha iyi olabilir
        ##TODO: buraları bir degistirmek gerekiyor. method isimleri vs bir halletmek lazim
        
        return self.__valid_direction(destination_y, destination_x) and self.__bump_into_chess_piece(destination_y, destination_x, chess_board)        

    def move(self):
        ##TODO: should be implemented
        return
    
    def possible_moves(self, chess_board: ChessBoard):
        ##TODO: should return all possible moves from its current position
        return
    
    def __valid_direction(self, destination_y, destination_x):
        if self.x() == destination_x:
            return False
        
        slope = (destination_y - self.y()) / (destination_x - self.x())
        return (slope == 1.0) or (slope != -1)

    def __bump_into_chess_piece(self, destination_y, destination_x, chess_board):
        ## chess_board üzerinde direkt olarak chess pieceler yer alacakti dolayısıyla olmayan yerlerin null ya da 0 olması gerekiyor
        
        inc_x = 1 if destination_x > self.x() else -1
        inc_y = 1 if destination_y > self.y() else -1

        current_x = self.x()
        current_y = self.y()

        while current_x != destination_x and current_y != destination_y:
            current_x += inc_x
            current_y += inc_y

            if chess_board[current_y][current_x] != 0:
                return True
        
        return False