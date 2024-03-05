from domain.ship import Ship
from domain.shot import Shot
from validators_and_exceptions import ShipValidator, BoardError, RepositoryException


class Board:
    def __init__(self, player, opponent, w, h, player_repository, ship_repository, shot_repository):
        self.__player = player
        self.__opponent = opponent
        self.__w = w
        self.__h = h
        self.__player_repository = player_repository
        self.__ship_repository = ship_repository
        self.__shot_repository = shot_repository

    def get_player(self):
        return self.__player

    def __check_if_ship_out_of_bounds(self, ship):
        """
        Checks if the ship is in the boundaries of the board
        :param ship:
        :return:
        """
        x = ship.get_x()
        y = ship.get_y()
        if x < 0 or x >= self.__h or y < 0 or y >= self.__w:
            raise BoardError("The ship is out of bounds !")

        tail_x = ship.get_tail_x()
        tail_y = ship.get_tail_y()
        if tail_x < 0 or tail_x >= self.__h or tail_y < 0 or tail_y >= self.__w:
            raise BoardError("The ship is out of bounds !")

    def __check_if_shot_out_of_bounds(self, shot):
        """
        Checks if the ship is in the boundaries of the board
        :param ship:
        :return:
        """
        x = shot.get_x()
        y = shot.get_y()
        if x < 0 or x >= self.__h or y < 0 or y >= self.__w:
            raise BoardError("The shot is out of bounds !")

    def __check_if_ship_overlaps(self, ship):
        """
        Checks if the ship overlaps with another already existent ship
        :param ship:
        :return:
        """
        ships = self.__ship_repository.get_all()
        for ship1 in ships:
            if ship1.overlaps(ship):
                raise BoardError(f"The ship overlaps with ship {ship1} !")

    def __check_shot_player(self, shot):
        """
        Checks if the shot made is on another player than the player itself, raises BoardError otherwise
        :param shot:
        :return:
        """
        if self.__player == shot.get_player():
            raise BoardError("Invalid shot player")

    def add_ship(self, length, direction, x, y):
        """
        Adds a ship to the board
        :param length:
        :param direction:
        :param x:
        :param y:
        :return:
        """
        ship = Ship(x, y, direction, length, self.__player,)
        ShipValidator.validate_ship(ship)
        self.__check_if_ship_out_of_bounds(ship)
        self.__check_if_ship_overlaps(ship)
        self.__ship_repository.add(ship)

    def add_shot(self, player, x, y):
        """
        Adds a shot to the board
        :param player:
        :param x:
        :param y:
        :return:
        """
        shot = Shot(x, y, player)
        self.__check_if_shot_out_of_bounds(shot)
        self.__check_shot_player(shot)
        self.__shot_repository.add(shot)

    def __str__(self):
        """
        Returns a string of the board which will be printed
        :return:
        """
        board_str = f"{self.__player.get_name()}: \n"
        ships = [x for x in self.__ship_repository.get_all() if x.get_player() == self.__player]
        for x in range(0, self.__h):
            for y in range(0, self.__w):
                opponent_shot = Shot(self.__opponent, x, y)
                try:
                    self.__shot_repository.search(opponent_shot)
                    board_str += "*"
                except RepositoryException:
                    ok = False
                    for ship in ships:
                        if ship.contains(x, y):
                            board_str += "="
                            ok = True
                            break
                    if not ok:
                        board_str += "~"
            board_str += "\n"
        board_str += "\n"
        for x in range(0, self.__h):
            for y in range(0, self.__w):
                self_shot = Shot(self.__player, x, y)
                try:
                    self.__shot_repository.search(self_shot)
                    board_str += "*"
                except RepositoryException:
                    board_str += "~"
            board_str += "\n"

        return board_str












