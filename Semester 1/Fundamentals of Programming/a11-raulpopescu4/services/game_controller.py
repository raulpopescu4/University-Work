from validators_and_exceptions import ControllerError


class GameController:
    def __init__(self, player_repository, shot_repository, ship_repository):
        self.__player_repository = player_repository
        self.__shot_repository = shot_repository
        self.__ship_repository = ship_repository
        self.__game_stats = dict()
        self.__ships_down = dict()
        self.__game_over = False
        self.__winner = None
        self.__initialize()

    def __initialize(self):
        for player in self.__player_repository.get_all():
            self.__game_stats[player.get_player_id()] = {2: [], 3: [], 4: [], 5: []}
            self.__ships_down[player.get_player_id()] = 0

    def game_over(self):
        pass

    def get_winner(self):
        pass

    def check(self, opponent, player):
        last_shot = self.__shot_repository.get_all()[-1]
        player_stats = self.__game_stats[opponent.get_player_id()]
        ships = [x for x in self.__ship_repository.get_all if x.get_player() == opponent]
        x = last_shot.get_x()
        y = last_shot.get_y()
        for ship in ships:
            if ship.contains(x, y):
                length = ship.get_length()
                if (x, y) in player_stats[length]:
                    raise ControllerError("You have already shot this position !")
                player_stats[length].append((x, y))
                if len(player_stats[length]) == length:
                    self.__ships_down[opponent.get_player_id()] += 1
                    if self.__ships_down[opponent.get_player_id()] == 3:
                        self.__game_over = True
                        self.__winner = player
