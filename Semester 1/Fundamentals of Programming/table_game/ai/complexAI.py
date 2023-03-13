from ai.basicAI import BasicAI
from settings.constants import SHIP, SEA


class ComplexAI(BasicAI):
    def __init__(self, board):
        BasicAI.__init__(self, board)

    def _hunt_for_next_hit_position(self):
        heat_map = [[0 for row in range(self._board.get_width())] for column in range(self._board.get_height())]

        for ship in self._board.get_ships():
            for direction in [self.get_position_from_north, self.get_position_from_south, self.get_position_from_west, self.get_position_from_east]:
                for x_coordinate in range(self._board.get_height()):
                    for y_coordinate in range(self._board.get_width()):
                        good_position = True
                        position = (x_coordinate, y_coordinate)
                        visited_positions = []

                        for length_iterator in range(len(ship)):
                            if not self.check_valid_position(position) or self._board.get_board()[x_coordinate][y_coordinate] not in [SEA, SHIP]:
                                good_position = False
                                break
                            visited_positions.append((x_coordinate, y_coordinate))
                            position = direction(position)

                        if good_position:
                            for position_iterator in visited_positions:
                                heat_map[position_iterator[0]][position_iterator[1]] += 1

        maximum_probability = 0
        most_likely_choices = list()

        for x_coordinate in range(self._board.get_height()):
            for y_coordinate in range(self._board.get_width()):
                if self._board.get_board()[x_coordinate][y_coordinate] in [SEA, SHIP]:
                    maximum_probability = max(maximum_probability, heat_map[x_coordinate][y_coordinate])

        for x_coordinate in range(self._board.get_height()):
            for y_coordinate in range(self._board.get_width()):
                if heat_map[x_coordinate][y_coordinate] == maximum_probability and self._board.get_board()[x_coordinate][y_coordinate] in [SEA, SHIP]:
                    most_likely_choices.append((x_coordinate, y_coordinate))
                    
        from random import choice
        return choice(most_likely_choices)
