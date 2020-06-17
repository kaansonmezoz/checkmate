from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.game.game_images import GameImages

import pygame
from pygame.locals import *

class GameScreen:
    def __init__(self):
        # pygame.error: No video mode has been set hatası aldim.
        # bunu cozmek icin basta sallamasyon bir display mode olusturdum.

        # ekrana bastirilmis olan taslar da burada olsun (baslangic_x, baslangic_y) seklinde tutularak
        # bu sayede biri ekranda basinca bir seye direkt olarak ilgili tasi bulabilelim.
        # o ilgili tasi da board'a geceriz ve orada ilgili islemlerin yapilmasini saglariz tasin hareketi gibi
        # ama bu durumda da bu hareket bitince o tasin image'nin bulundugu konumu silmek gerekecek
        # bir de cok fazla data share edilmis olacak bu fikirden caydim.
        # en temizi board'dan yerlerini alalim taslarin sonra da gidip image'larını aliriz
        # dolayısıyla buradaki chess_piece_image arkada board üzerinde bir chess_piece'e denk gelsin
        # ya da sürekli olarak burada image ekleyelim verilen koordinata diger secenek de bu


        self.__pygame = pygame
        self.__pygame.init()
        self.__screen = pygame.display.set_mode((600,600))
        self.__game_images = GameImages(pygame)        
        self.__init_screen()
        ## blit sadece cizdiriyor ekrani.
        self.__screen.blit(self.__game_images.board(),(0,0))

        ## Oyun tahtasindaki karenin boyutları
        self.__square_height = 0 # boarddaki bir karenin yuksekligi
        self.__square_width = 0  # boarddaki bir karenin genisligi

        # butun degisiklikleri vs renderlamak icin bunu yapmak lazim yani update'i cagirtmak lazim        
        pygame.display.update() 
    
    def __init_screen(self):        
        size = self.__game_images.board_size()
        self.__pygame.display.set_caption('Checkmate')
        screen = self.__pygame.display.set_mode(size)
        screen.blit(self.__game_images.board(), (0, 0))
        self.__screen = screen

    def update(self, white_pieces, black_pieces):
        # bütün taslarin konumlari alinmali
        # once board uzerinde bu taslar konulmalı
        # sonrasında da bunları renderlamak gerekiyor.

        # Daha iyi bir cozum lazim

        self.__clear_screen()
        self.__screen.blit(self.__game_images.board(), (0, 0))

        self.__put_pieces(white_pieces, self.__square_width, self.__square_height)
        self.__put_pieces(black_pieces, self.__square_width, self.__square_height)

        self.__pygame.display.update()
    
    def __clear_screen(self):
        black = (0, 0, 0)
        self.__screen.fill(black)
    
    def __put_pieces(self, pieces, square_width, square_height):
        for piece in pieces:
            location = (piece.x() * square_width, piece.y() * square_height)
            image = self.__game_images.piece_image(piece.color(), piece.get_type())
            self.__screen_blit(image, location)
