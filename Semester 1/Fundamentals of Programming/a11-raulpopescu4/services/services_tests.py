import unittest

from persistency.repository import Repository
from services.board import Board


class BoardTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__player_repository = Repository()
        self.__shot_repository = Repository()
        self.__ship_repository = Repository()
        self.__board = Board(1, 2, 10, 10, self.__player_repository, self.__ship_repository, self.__shot_repository)

    def test_add_ship(self):
        self.__board.add_ship(3, 0, 4, 5)
        self.assertEqual(len(self.__ship_repository.get_all()), 1)

    def test_add_shot(self):
        self.__board.add_shot(2, 3, 4)
        self.assertEqual(len(self.__shot_repository.get_all()), 1)

    def tearDown(self) -> None:
        pass
