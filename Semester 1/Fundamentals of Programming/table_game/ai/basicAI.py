from settings.constants import SHIP, HIT, SEA


class BasicAI:
    def __init__(self, board):
        self._board = board

    # parity check of a random shot's coordinates(shot that is not registered as a hit already)
    def _hunt_for_next_hit_position(self):
        board_height = self._board.get_height()
        board_width = self._board.get_width()

        from random import randrange
        x_coordinate = randrange(board_height)
        y_coordinate = randrange(board_width)

        while self._board.get_board()[x_coordinate][y_coordinate] not in [SHIP, SEA] or (x_coordinate + y_coordinate) % 2 == 1:
            x_coordinate = randrange(board_height)
            y_coordinate = randrange(board_width)

        position = (x_coordinate, y_coordinate)
        return position

    @staticmethod
    def get_position_from_north(position):
        x_coordinate = position[0] - 1
        y_coordinate = position[1]
        position_from_north = (x_coordinate, y_coordinate)
        return position_from_north

    @staticmethod
    def get_position_from_east(position):
        x_coordinate = position[0]
        y_coordinate = position[1] + 1
        position_from_east = (x_coordinate, y_coordinate)
        return position_from_east

    @staticmethod
    def get_position_from_south(position):
        x_coordinate = position[0] + 1
        y_coordinate = position[1]
        position_from_south = (x_coordinate, y_coordinate)
        return position_from_south

    @staticmethod
    def get_position_from_west(position):
        x_coordinate = position[0]
        y_coordinate = position[1] - 1
        position_from_west = (x_coordinate, y_coordinate)
        return position_from_west

    def check_valid_position(self, position):
        x_coordinate = position[0]
        y_coordinate = position[1]

        board_height = self._board.get_height()
        board_width = self._board.get_width()

        return x_coordinate in range(0, board_height) and y_coordinate in range(0, board_width)

    # hunt and target next position
    def _target_next_position_based_on_hit(self, actual_position):
        horizontal_direction = True
        vertical_direction = True

        def try_direction(direction, position):
            next_position = direction(position)
            x_coordinate = next_position[0]
            y_coordinate = next_position[1]
            while self.check_valid_position(next_position) and self._board.get_board()[x_coordinate][y_coordinate] is HIT:
                next_position = direction(next_position)
            if self.check_valid_position(next_position) and self._board.get_board()[x_coordinate][y_coordinate] in [SHIP, SEA]:
                return next_position

        def search_on_horizontal():
            if try_direction(self.get_position_from_west, actual_position):
                return try_direction(self.get_position_from_west, actual_position)
            if try_direction(self.get_position_from_east, actual_position):
                return try_direction(self.get_position_from_east, actual_position)

        def search_on_vertical():
            if try_direction(self.get_position_from_north, actual_position):
                return try_direction(self.get_position_from_north, actual_position)
            if try_direction(self.get_position_from_south, actual_position):
                return try_direction(self.get_position_from_south, actual_position)

        west_x_coordinate = self.get_position_from_west(actual_position)[0]
        west_y_coordinate = self.get_position_from_west(actual_position)[1]

        east_x_coordinate = self.get_position_from_east(actual_position)[0]
        east_y_coordinate = self.get_position_from_east(actual_position)[1]

        if (self.check_valid_position(self.get_position_from_west(actual_position)) and self._board.get_board()[west_x_coordinate][west_y_coordinate] is HIT) or\
                (self.check_valid_position(self.get_position_from_east(actual_position)) and self._board.get_board()[east_x_coordinate][east_y_coordinate] is HIT):
            vertical_direction = False

        north_x_coordinate = self.get_position_from_north(actual_position)[0]
        north_y_coordinate = self.get_position_from_north(actual_position)[1]

        south_x_coordinate = self.get_position_from_south(actual_position)[0]
        south_y_coordinate = self.get_position_from_south(actual_position)[1]

        if (self.check_valid_position(self.get_position_from_south(actual_position)) and self._board.get_board()[south_x_coordinate][south_y_coordinate] is HIT) or\
                (self.check_valid_position(self.get_position_from_north(actual_position)) and self._board.get_board()[north_x_coordinate][north_y_coordinate] is HIT):
            horizontal_direction = False

        if horizontal_direction:
            if search_on_horizontal():
                return search_on_horizontal()

        if vertical_direction:
            if search_on_vertical():
                return search_on_vertical()

        if search_on_horizontal():
            return search_on_horizontal()

        if search_on_vertical():
            return search_on_vertical()

        return None

    def find_the_best_next_move(self):
        board_height = self._board.get_height()
        board_width = self._board.get_width()

        for x_coordinate in range(board_height):
            for y_coordinate in range(board_width):
                if self._board.get_board()[x_coordinate][y_coordinate] is HIT:

                    position_to_attack = self._target_next_position_based_on_hit((x_coordinate, y_coordinate))

                    if position_to_attack is not None:
                        return position_to_attack

        return self._hunt_for_next_hit_position()
