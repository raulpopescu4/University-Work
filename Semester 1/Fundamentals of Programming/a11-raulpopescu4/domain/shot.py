class Shot:
    def __init__(self, x, y, player):
        self.__x = x
        self.__y = y
        self.__player = player

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_player(self):
        return self.__player

    def __eq__(self, other):
        return self.__x == other.get_x() and self.__y == other.get_y() and self.__player == other.get_player()




