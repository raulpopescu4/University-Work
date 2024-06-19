class Player:
    def __init__(self, player_id, name):
        self.__player_id = player_id
        self.__name = name

    def get_player_id(self):
        return self.__player_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __eq__(self, other):
        return self.__player_id == other.get_player_id()

