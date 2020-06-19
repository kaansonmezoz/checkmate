from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.chess.pieces.chess_piece import ChessPiece

class ChessBoard:
    def __init__(self):
        self.__board = [[0] * 8 for _ in range(8)]
        self.__white_pieces = []
        self.__black_pieces = []
        self.__fill_board(self.__white_pieces, self.__black_pieces)

    def __fill_board(self, white_pieces, black_pieces):
        self.__put_black_chess_pieces(white_pieces)
        self.__put_white_chess_pieces(black_pieces)
    
    def __put_white_chess_pieces(self, white_pieces):
        self.__put_chess_pieces(white_pieces, 'white', 0, 1)

    def __put_black_chess_pieces(self, black_pieces):
        self.__put_chess_pieces(black_pieces, 'black', 7, 6)

    def __put_chess_pieces(self, pieces, color, y1, y2):
        self.__board[y1][0] = self.__create_chess_piece(pieces, ChessPiece.rook, 'rook', color,'1', y1, 0)
        self.__board[y1][1] = self.__create_chess_piece(pieces, ChessPiece.knight, 'knight', color, '1', y1, 1)
        self.__board[y1][2] = self.__create_chess_piece(pieces, ChessPiece.bishop, 'bishop', color, '1', y1, 2)
        self.__board[y1][3] = self.__create_chess_piece(pieces, ChessPiece.queen, 'queen', color, '1', y1, 3)
        self.__board[y1][4] = self.__create_chess_piece(pieces, ChessPiece.king, 'king', color, '1' ,y1, 4)
        self.__board[y1][5] = self.__create_chess_piece(pieces, ChessPiece.bishop, 'bishop', color, '2', y1, 5)
        self.__board[y1][6] = self.__create_chess_piece(pieces, ChessPiece.knight, 'knight', color, '2', y1, 6)
        self.__board[y1][7] = self.__create_chess_piece(pieces, ChessPiece.rook, 'rook', color, '2', y1, 7)

        for x in range(8):
            self.__board[y2][x] = self.__create_chess_piece(pieces, ChessPiece.pawn, 'pawn', color, str(x+1), y2, x)

    def __create_chess_piece(self, pieces, creator, piece_type, color, number, y, x):
        piece = creator(piece_type, color, number, y, x)
        pieces.append(piece)
        return piece

    def white_pieces(self):
        return self.__white_pieces
    
    def black_pieces(self):
        return self.__black_pieces
    
    def chess_piece(self, y, x):
        return self.__board[y][x]

    def move_chess_piece(self, chess_move: ChessMove):      
        chess_piece = chess_move.chess_piece()
        destination = chess_move.destination()
        y = destination['y']
        x = destination['x']
        
        # TODO: Rest of the function should be implemented
                
        return

    def game_not_finished(self):
        ## should be implemented
        return True