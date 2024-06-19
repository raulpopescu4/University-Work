import unittest

from src.domain.client import Client
from src.domain.movie import Movie
from src.domain.rental import Rental
from src.repository.client_repository import ClientRepository
from src.repository.movie_repository import MovieRepository
from src.repository.rental_repository import RentalRepository
from src.exceptions_and_validators.exceptions import RepositoryException


class ClientRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.__client_repository = ClientRepository()

    def test_search(self):
        client = Client("3", "aaa")
        self.__client_repository.add(client)
        self.assertEqual(self.__client_repository.search(client.get_id()), client)

    def test_search_exception(self):
        client = Client("3", "aaa")
        self.__client_repository.add(client)
        with self.assertRaises(RepositoryException):
            self.__client_repository.search("18")

    def test_add(self):
        client = Client("3", "aaa")
        self.__client_repository.add(client)
        self.assertEqual(len(self.__client_repository), 1)

    def test_add_exception(self):
        client1 = Client("3", "aaa")
        self.__client_repository.add(client1)
        client2 = Client("3", "bbb")
        with self.assertRaises(RepositoryException):
            self.__client_repository.add(client2)

    def test_update(self):
        client = Client("3", "aaa")
        self.__client_repository.add(client)
        updated_client = Client("3", "bbb")
        self.__client_repository.update(updated_client)
        self.assertEqual(self.__client_repository.search(client.get_id()), updated_client)

    def test_update_exception(self):
        client1 = Client("3", "aaa")
        self.__client_repository.add(client1)
        client2 = Client("5", "bbb")
        with self.assertRaises(RepositoryException):
            self.__client_repository.update(client2)

    def test_remove(self):
        client = Client("3", "aaa")
        self.__client_repository.add(client)
        self.__client_repository.remove("3")
        self.assertEqual(len(self.__client_repository), 0)

    def test_remove_exception(self):
        client = Client("3", "aaa")
        self.__client_repository.add(client)
        with self.assertRaises(RepositoryException):
            self.__client_repository.remove("5")

    def test_get_all(self):
        self.assertEqual(str(self.__client_repository.get_all()), 'dict_values([])')

    def tearDown(self) -> None:
        pass


class MovieRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.__movie_repository = MovieRepository()

    def test_search(self):
        movie = Movie("3", "aaa", "bbb", "ccc")
        self.__movie_repository.add(movie)
        self.assertEqual(self.__movie_repository.search(movie.get_id()), movie)

    def test_search_exception(self):
        movie = Movie("3", "aaa", "bbb", "ccc")
        self.__movie_repository.add(movie)
        with self.assertRaises(RepositoryException):
            self.__movie_repository.search("18")

    def test_add(self):
        movie = Movie("3", "aaa", "bbb", "ccc")
        self.__movie_repository.add(movie)
        self.assertEqual(len(self.__movie_repository), 1)

    def test_add_exception(self):
        movie = Movie("3", "aaa", "bbb", "ccc")
        self.__movie_repository.add(movie)
        movie2 = Movie("3", "vvv", "bbb", "ddd")
        with self.assertRaises(RepositoryException):
            self.__movie_repository.add(movie2)

    def test_update(self):
        movie = Movie("3", "aaa", "bbb", "ccc")
        self.__movie_repository.add(movie)
        updated_movie = Movie("3", "vvv", "sss", "aaa")
        self.__movie_repository.update(updated_movie)
        self.assertEqual(self.__movie_repository.search(movie.get_id()), updated_movie)

    def test_update_exception(self):
        movie = Movie("3", "aaa", "bbb", "ccc")
        self.__movie_repository.add(movie)
        movie2 = Movie("5", "vvv", "sss", "aaa")
        with self.assertRaises(RepositoryException):
            self.__movie_repository.update(movie2)

    def test_remove(self):
        movie = Movie("3", "aaa", "bbb", "ccc")
        self.__movie_repository.add(movie)
        self.__movie_repository.remove("3")
        self.assertEqual(len(self.__movie_repository), 0)

    def test_remove_exception(self):
        movie = Movie("3", "aaa", "bbb", "ccc")
        self.__movie_repository.add(movie)
        with self.assertRaises(RepositoryException):
            self.__movie_repository.remove("5")

    def test_get_all(self):
        self.assertEqual(str(self.__movie_repository.get_all()), 'dict_values([])')

    def tearDown(self) -> None:
        pass


class RentalRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.__rental_repository = RentalRepository()

    def test_search(self):
        rental = Rental("1", "3", "7", "2021-07-08", "2021-11-12", "2022-01-02")
        self.__rental_repository.add(rental)
        self.assertEqual(self.__rental_repository.search(rental.get_id()), rental)

    def test_search_exception(self):
        rental = Rental("1", "3", "7", "2021-07-08", "2021-11-12", "2022-01-02")
        self.__rental_repository.add(rental)
        with self.assertRaises(RepositoryException):
            self.__rental_repository.search("18")

    def test_add(self):
        rental = Rental("1", "3", "7", "2021-07-08", "2021-11-12", "2022-01-02")
        self.__rental_repository.add(rental)
        self.assertEqual(len(self.__rental_repository), 1)

    def test_add_exception(self):
        rental = Rental("1", "3", "7", "2021-07-08", "2021-11-12", "2022-01-02")
        self.__rental_repository.add(rental)
        rental2 = Rental("1", "11", "25", "2022-07-08", "2022-11-12", "2023-01-02")
        with self.assertRaises(RepositoryException):
            self.__rental_repository.add(rental2)

    def test_update(self):
        rental = Rental("1", "3", "7", "2021-07-08", "2021-11-12", "2022-01-02")
        self.__rental_repository.add(rental)
        updated_rental = Rental("1", "11", "25", "2022-07-08", "2022-11-12", "2023-01-02")
        self.__rental_repository.update(updated_rental)
        self.assertEqual(self.__rental_repository.search(rental.get_id()), updated_rental)

    def test_update_exception(self):
        rental = Rental("1", "3", "7", "2021-07-08", "2021-11-12", "2022-01-02")
        self.__rental_repository.add(rental)
        rental2 = Rental("3", "11", "25", "2022-07-08", "2022-11-12", "2023-01-02")
        with self.assertRaises(RepositoryException):
            self.__rental_repository.update(rental2)

    def test_remove(self):
        rental = Rental("1", "3", "7", "2021-07-08", "2021-11-12", "2022-01-02")
        self.__rental_repository.add(rental)
        self.__rental_repository.remove("1")
        self.assertEqual(len(self.__rental_repository), 0)

    def test_remove_exception(self):
        rental = Rental("1", "3", "7", "2021-07-08", "2021-11-12", "2022-01-02")
        self.__rental_repository.add(rental)
        with self.assertRaises(RepositoryException):
            self.__rental_repository.remove("5")

    def test_get_all(self):
        self.assertEqual(str(self.__rental_repository.get_all()), 'dict_values([])')

    def tearDown(self) -> None:
        pass
