from validators_and_exceptions import BoardError, ValidationError


class Console:
    def __init__(self, board1, board2, game_controller):
        self.__board1 = board1
        self.__board2 = board2
        self.__game_controller = game_controller

    def __set_initial_board(self, board):
        for len in [2, 3, 4, 5]:
            try:
                direction = int(input(f"Give a direction (0, 1, 2, 3) for the ship of length {len}: "))
            except ValueError as ve:
                print(f" The direction value must be an integer \n {ve} ")
                break
            while True:
                try:
                    x = int(input("Give the head of the ship the x coordinate: "))
                    y = int(input("Give the head of the ship the y coordinate: "))
                except ValueError as ve:
                    print(f"Invalid value! x, y must be integers \n {ve}")
                try:
                    board.add_ship(len, direction, x, y)
                    break
                except BoardError as be:
                    print(f"Board Error: \n {be}")
                except ValidationError as ve:
                    print(f"Validation Error: \n {ve}")

    def __print_boards(self):
        print(self.__board1)
        print(self.__board2)

    def run(self):
        print("Player one")
        self.__set_initial_board(self.__board1)
        print("Player two")
        self.__set_initial_board(self.__board2)
        player1 = self.__board1.get_player()
        player2 = self.__board2.get_player()
        while True:
            self.__print_boards()
            print("Player one")
            try:
                x = int(input(f"Give the shot x coordinate: "))
                y = int(input(f"Give the shot y coordinate: "))
                self.__board2.add_hit(player1, x, y)
                self.__game_controller.check(player2, player1)
            except ValueError as ve:
                print(f"Invalid value! x, y must be integers \n {ve}")
            except BoardError as be:
                print(f"Board2 error: \n {be}")
            if self.__game_controller.game_over():
                print(f"{self.__game_controller.get_winner()} has won!")
                return
            print("Player two")
            try:
                x = int(input(f"Give the shot x coordinate: "))
                y = int(input(f"Give the shot y coordinate: "))
                self.__board1.add_hit(player2, x, y)
                self.__game_controller.check(player1, player2)
            except ValueError as ve:
                print(f"Invalid value! x, y must be integers \n {ve}")
            except BoardError as be:
                print(f"Board1 error: \n {be}")
            if self.__game_controller.game_over():
                print(f"{self.__game_controller.get_winner()} has won!")
                return










