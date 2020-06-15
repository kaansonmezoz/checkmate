from .pieces.chess_piece import ChessPiece

class ChessBoard:
    def __init__(self):
        self.__board = [[0] * 8 for _ in range(8)]
        self.__fill_board()

    def __fill_board(self):
        self.__put_black_chess_pieces()
        self.__put_white_chess_pieces()
    
    def __put_white_chess_pieces(self):
        self.__put_chess_pieces('white', 0, 1)

    def __put_black_chess_pieces(self):
        self.__put_chess_pieces('black', 6, 7)

    def __put_chess_pieces(self, color, x1, x2):
        self.__board[x1][0] = ChessPiece.rook('rook_1', color, x1, 0)
        self.__board[x1][1] = ChessPiece.knight('knight_1', color, x1, 1)
        self.__board[x1][2] = ChessPiece.bishop('bishop_1', color, x1, 2)
        self.__board[x1][3] = ChessPiece.queen('queen', color, x1, 3)
        self.__board[x1][4] = ChessPiece.king('king', color, x1, 4)
        self.__board[x1][5] = ChessPiece.bishop('bishop_2', color, x1, 5)
        self.__board[x1][6] = ChessPiece.knight('knight_2', color, x1, 6)
        self.__board[x1][7] = ChessPiece.rook('rook_2', color, x1, 7)

        for y in range(8):
            self.__board[x2][y] = ChessPiece.pawn('pawn_' + str(y+1), color, x2, y)