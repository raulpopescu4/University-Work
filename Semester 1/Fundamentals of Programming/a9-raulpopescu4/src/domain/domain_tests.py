import unittest
from src.domain.client import Client
from src.domain.movie import Movie
from src.domain.rental import Rental, RentalDTO, RentalMovieStatisticsDTO, RentalClientStatisticsDTO


class ClientTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_client = Client("2", "aaa")
        self.__test_client2 = Client("2", "aaa")

    def test_client_id_getter(self):
        self.assertEqual(self.__test_client.get_id(), "2")

    def test_name_getter(self):
        self.assertEqual(self.__test_client.get_name(), "aaa")

    def test_name_setter(self):
        self.__test_client.set_name("bbb")
        self.assertEqual(self.__test_client.get_name(), "bbb")

    def test_eq(self):
        self.assertEqual(self.__test_client, self.__test_client2)

    def test_str(self):
        self.assertEqual(self.__test_client.__str__(), "2 - aaa")

    def tearDown(self) -> None:
        pass


class MovieTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_movie = Movie("5", "aaa", "bbb", "ccc")
        self.__test_movie2 = Movie("5", "aaa", "bbb", "ccc")
        self._test_movie3 = Movie("12", "vvv", "nnn", "sss")

    def test_movie_id_getter(self):
        self.assertEqual(self.__test_movie.get_id(), "5")

    def test_movie_title_getter(self):
        self.assertEqual(self._test_movie3.get_title(), "vvv")

    def test_movie_title_setter(self):
        self._test_movie3.set_title("ooo")
        self.assertEqual(self._test_movie3.get_title(), "ooo")

    def test_movie_description_getter(self):
        self.assertEqual(self.__test_movie.get_description(), "bbb")

    def test_movie_description_setter(self):
        self.__test_movie.set_description("ooo")
        self.assertEqual(self.__test_movie.get_description(), "ooo")

    def test_movie_genre_getter(self):
        self.assertEqual(self._test_movie3.get_genre(), "sss")

    def test_movie_genre_setter(self):
        self._test_movie3.set_genre("ooo")
        self.assertEqual(self._test_movie3.get_genre(), "ooo")

    def test_eq(self):
        self.__test_movie2.set_description("bbb")
        self.assertEqual(self.__test_movie, self.__test_movie2)

    def test_str(self):
        self.assertEqual(self.__test_movie.__str__(), "5 - aaa - bbb - ccc")

    def tearDown(self) -> None:
        pass


class RentalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_rental = Rental("2", "31", "49", "2021-02-08", "2022-03-01", "2021-11-12")
        self.__test_rental2 = Rental("2", "31", "49", "2021-02-08", "2022-03-01", "2021-11-12")
        self.__test_rental3 = Rental("17", "1", "5", "2021-04-11", "2021-07-11", "2022-01-02")

    def test_rental_id_getter(self):
        self.assertEqual(self.__test_rental.get_id(), "2")

    def test_movie_id_getter(self):
        self.assertEqual(self.__test_rental3.get_movie_id(), "1")

    def test_client_id_getter(self):
        self.assertEqual(self.__test_rental.get_client_id(), "49")

    def test_rented_date_getter(self):
        self.assertEqual(self.__test_rental3.get_rented_date(), "2021-04-11")

    def test_rented_date_setter(self):
        self.__test_rental3.set_rented_date("2023-01-05")
        self.assertEqual(self.__test_rental3.get_rented_date(), "2023-01-05")

    def test_due_date_getter(self):
        self.assertEqual(self.__test_rental.get_due_date(), "2022-03-01")

    def test_due_date_setter(self):
        self.__test_rental.set_due_date("2022-02-12")
        self.assertEqual(self.__test_rental.get_due_date(), "2022-02-12")

    def test_returned_date_getter(self):
        self.assertEqual(self.__test_rental3.get_returned_date(), "2022-01-02")

    def test_returned_date_setter(self):
        self.__test_rental3.set_returned_date("2011-11-11")
        self.assertEqual(self.__test_rental3.get_returned_date(), "2011-11-11")

    def test_eq(self):
        self.assertEqual(self.__test_rental, self.__test_rental2)

    def test_str(self):
        self.assertEqual(self.__test_rental.__str__(), "2 - 31 - 49 - 2021-02-08 - 2022-03-01 - 2021-11-12")

    def tearDown(self) -> None:
        pass


class RentalDTOTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__rental_dto_test = RentalDTO(1, "aaa", "bbb", "2021-02-08", "2022-03-01", "2021-11-12")

    def test_str(self):
        self.assertEqual(self.__rental_dto_test.__str__(), "1 - aaa - bbb - 2021-02-08 - 2022-03-01 - 2021-11-12")

    def tearDown(self) -> None:
        pass


class RentalMovieStatisticsDTOTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__dto1 = RentalMovieStatisticsDTO("aaa", 1)
        self.__dto2 = RentalMovieStatisticsDTO("aaa", 7)

    def test_str_one_day(self):
        self.assertEqual(self.__dto1.__str__(), "aaa - 1 day")

    def test_str_multiple_days(self):
        self.assertEqual(self.__dto2.__str__(), "aaa - 7 days")

    def tearDown(self) -> None:
        pass


class RentalClientStatisticsDTOTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__dto1 = RentalClientStatisticsDTO("aaa", 1)
        self.__dto2 = RentalClientStatisticsDTO("aaa", 5)

    def test_str_one_day(self):
        self.assertEqual(self.__dto1.__str__(), "aaa - 1 day")

    def test_str_multiple_days(self):
        self.assertEqual(self.__dto2.__str__(), "aaa - 5 days")

    def tearDown(self) -> None:
        pass
