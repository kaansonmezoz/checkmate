from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

import os

# buradaki mediayı farklı bir sekilde saklamak gerekli aslinda
# yani bu class sadece okumayı saglasin ve isi bitsin olmali
# asil game_board vs gibi bir seyde olmali sanki bu image'lar
# hatta iki tip image olsun. GameImages, MenuImages gibi
class GameImages:
    def __init__(self, pygame):
        self.__pygame = pygame
        self.__board = pygame.image.load(os.path.join(os.path.dirname(__file__), '../../assets/board.png')).convert()
        self.__square_width, self.__square_height = self.__get_board_square_size()
        self.__load_chess_board_images(pygame)
        self.__load_menu_images(pygame)

    def __get_board_square_size(self):
        size = self.board_size()
        return size[0]/8, size[1]/8

    def __load_chess_board_images(self, pygame):                
        w, h = self.__square_width, self.__square_height
        self.__pieces = self.__load_image('../../assets/Chess_Pieces_Sprite.png', w, h)
        self.__green_circle = self.__load_image('../../assets/Chess_Pieces_Sprite.png', w, h)
        self.__red_circle = self.__load_image('../../assets/red_circle_big.png', w, h)        
        self.__green_box = self.__load_image('../../assets/green_box.png', w, h)        
        self.__yellow_circle = self.__load_image('../../assets/yellow_circle_big.png', w, h)    
        self.__green_big_circle = self.__load_image('../../assets/green_circle_big.png', w, h)
        self.__yellow_box = self.__load_image('../../assets/yellow_box.png', w, h)

    def __load_menu_images(self, pygame):
        w, h = self.__square_width, self.__square_height      
        self.__friend = self.__load_image('../../assets/withfriend.png', w, h)
        self.__ai = self.__load_image('../../assets/withAI.png', w, h)
        self.__play_white = self.__load_image('../../assets/playWhite.png', w, h)    
        self.__play_black = self.__load_image('../../assets/playBlack.png', w, h)
        self.__flip_enabled = self.__load_image('../../assets/flipEnabled.png', w, h)
        self.__flip_disabled = self.__load_image('../../assets/flipDisabled.png', w, h)

    def __load_image(self, path, width, height):
        base_path = os.path.join(os.path.dirname(__file__))
        path = os.path.join(base_path, path)
        image = self.__pygame.image.load(path).convert_alpha()
        return self.__scale_image(image, width, height)

    def __scale_image(self, image, width, height):
        return self.__pygame.transform.scale(image, (int(width), int(height)))
    
    def board(self):
        return self.__board

    def board_size(self):
        return self.__board.get_rect().size