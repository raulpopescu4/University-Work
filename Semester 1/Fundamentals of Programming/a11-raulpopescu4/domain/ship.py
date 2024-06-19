

class Ship:
    def __init__(self, x, y, direction, length, player):
        self.__x = x
        self.__y = y
        self.__direction = direction
        self.__length = length
        self.__player = player

    __directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_direction(self):
        return self.__direction

    def get_length(self):
        return self.__length

    def get_player(self):
        return self.__player

    def get_tail_x(self):
        return self.__x + self.__directions[self.__direction][0] * self.__length

    def get_tail_y(self):
        return self.__y + self.__directions[self.__direction][1] * self.__length

    def contains(self, x, y):
        return self.__x <= x <= self.get_tail_x() and self.__y <= y <= self.get_tail_y()

    def overlaps(self, other):
        min_x = min(self.__x, self.get_tail_x()+1)
        max_x = max(self.__x, self.get_tail_x()+1)

        min_y = min(self.__y, self.get_tail_y() + 1)
        max_y = max(self.__y, self.get_tail_y() + 1)
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                if other.contains(x, y):
                    return True
        return False

    def __str__(self):
        return f"x: {self.__x}, y: {self.__y}, direction: {self.__direction} "
