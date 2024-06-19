from UI.console import Console
from domain.player import Player
from persistency.repository import Repository
from services.board import Board
from services.game_controller import GameController

if __name__ == '__main__':
    player_repository = Repository()
    ship_repository = Repository()
    shot_repository = Repository()

    player1 = Player(1, "dani")
    player2 = Player(2, "wow")

    player_repository.add(player1)
    player_repository.add(player2)

    w = 8
    h = 8

    board1 = Board(player1, player2, w, h, player_repository, shot_repository, ship_repository)
    board2 = Board(player2, player1, w, h, player_repository, shot_repository, ship_repository)

    game_controller = GameController(player_repository, shot_repository, ship_repository)

    console = Console(board1, board2, game_controller)

    console.run()
