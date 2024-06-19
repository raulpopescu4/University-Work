import unittest

from domain.player import Player
from domain.ship import Ship
from domain.shot import Shot


class PlayerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__player1 = Player(1, "dani")
        self.__player2 = Player(1, "dragonu")

    def test_get_name(self):
        self.assertEqual(self.__player1.get_name(), "dani")

    def test_set_name(self):
        self.__player1.set_name("mama")
        self.assertEqual(self.__player1.get_name(), "mama")

    def test_get_player_id(self):
        self.assertEqual(self.__player1.get_player_id(), 1)

    def test_eq(self):
        value1 = self.__player1.__eq__(self.__player2)
        value2 = self.__player1.get_player_id() == self.__player2.get_player_id()
        self.assertEqual(value1, value2)

    def tearDown(self) -> None:
        pass


class ShotTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__shot1 = Shot(1, 2, 1)
        self.__shot2 = Shot(1, 2, 1)

    def test_get_x(self):
        self.assertEqual(self.__shot1.get_x(), 1)

    def test_get_y(self):
        self.assertEqual(self.__shot1.get_y(), 2)

    def test_get_player(self):
        self.assertEqual(self.__shot1.get_player(), 1)

    def test_eq(self):
        value1 = self.__shot1.__eq__(self.__shot2)
        value2 = self.__shot1 == self.__shot2
        self.assertEqual(value1, value2)

    def tearDown(self) -> None:
        pass


class ShipTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__ship1 = Ship(1, 2, 3, 4, 5)
        self.__ship2 = Ship(1, 2, 3, 4, 5)

    def test_get_x(self):
        self.assertEqual(self.__ship1.get_x(), 1)

    def test_get_y(self):
        self.assertEqual(self.__ship1.get_y(), 2)

    def test_get_direction(self):
        self.assertEqual(self.__ship1.get_direction(), 3)

    def test_get_length(self):
        self.assertEqual(self.__ship1.get_length(), 4)

    def test_get_player(self):
        self.assertEqual(self.__ship1.get_player(), 5)

    def test_get_tail_x(self):
        self.assertEqual(self.__ship1.get_tail_x(), 1)

    def test_get_tail_y(self):
        self.assertEqual(self.__ship1.get_tail_y(), -2)

    def test_contains_true(self):
        self.assertEqual(self.__ship1.contains(1, 2), True)

    def test_contains_false(self):
        self.assertEqual(self.__ship1.contains(10, 9), False)

    def test_overlaps_true(self):
        self.assertEqual(self.__ship1.overlaps(self.__ship2), True)

    def test_overlaps_false(self):
        self.assertEqual(self.__ship1.overlaps(Ship(10, 9, 3, 4, 5)), False)



    def tearDown(self) -> None:
        pass
