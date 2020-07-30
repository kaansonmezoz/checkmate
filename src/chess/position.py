from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

class Position:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def x(self):
        return self.__x
    
    def y(self):
        return self.__y