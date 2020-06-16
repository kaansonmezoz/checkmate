from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from src.game.game_images import GameImages

class GameScreen:
    def __init__(self, pygame, chess_board):
        # pygame.error: No video mode has been set hatası aldim.
        # bunu cozmek icin basta sallamasyon bir display mode olusturdum.

        self.__pygame = pygame
        self.__screen = pygame.display.set_mode((600,600))
        self.__chess_board = chess_board
        self.__game_images = GameImages(pygame)        
        self.__init_screen()
        ## blit sadece cizdiriyor ekrani.
        self.__screen.blit(self.__game_images.board(),(0,0))
        # butun degisiklikleri vs renderlamak icin bunu yapmak lazim yani update'i cagirtmak lazim
        pygame.display.update() 


    
    def __init_screen(self):        
        size = self.__game_images.board_size()
        self.__pygame.display.set_caption('Checkmate')
        screen = self.__pygame.display.set_mode(size)
        screen.blit(self.__game_images.board(), (0, 0))
        self.__screen = screen

