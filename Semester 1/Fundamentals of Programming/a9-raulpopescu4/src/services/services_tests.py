import unittest

from src.domain.client import Client
from src.domain.movie import Movie
from src.domain.rental import Rental
from src.repository.client_repository import ClientRepository
from src.repository.movie_repository import MovieRepository
from src.repository.rental_repository import RentalRepository
from src.services.client_services import ClientServices
from src.services.movie_services import MovieServices
from src.exceptions_and_validators.exceptions import RepositoryException, ValidatorException
from src.services.rental_services import RentalServices
from src.services.undo_redo_services import UndoRedoServices


class ClientServicesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__client_repository = ClientRepository()
        self.__movie_repository = MovieRepository()
        self.__rental_repository = RentalRepository()
        self.__undo_redo_services = UndoRedoServices()
        self.__rental_services = RentalServices(self.__client_repository, self.__movie_repository, self.__rental_repository, self.__undo_redo_services)
        self.__client_services = ClientServices(self.__client_repository, self.__rental_services, self.__undo_redo_services)

    def test_add_client_exception(self):
        try:
            self.__client_services.add_client(14, "")
            assert False
        except ValidatorException as exception:
            self.assertEqual(len(exception.get_errors()), 1)

    def test_add_client_repository_exception(self):
        self.__client_repository.add(Client(14, "aaa"))
        with self.assertRaises(RepositoryException):
            self.__client_services.add_client(14, "bbb")

    def test_add_client(self):
        self.__client_services.add_client(14, "aaa")
        clients = self.__client_services.get_all_clients()
        self.assertEqual(len(clients), 1)

    def test_remove_client_exception(self):
        try:
            self.__client_services.remove_client(-14)
            assert False
        except ValidatorException as exception:
            self.assertEqual(len(exception.get_errors()), 1)

    def test_remove_client_repository_exception(self):
        with self.assertRaises(RepositoryException):
            self.__client_services.remove_client(14)

    def test_remove(self):
        self.__client_services.add_client(14, "Aaa")
        self.__client_services.remove_client(14)
        clients = self.__client_services.get_all_clients()
        self.assertEqual(len(clients), 0)

    def test_update_client_exception(self):
        try:
            self.__client_services.update_client(14, "")
            assert False
        except ValidatorException as exception:
            self.assertEqual(len(exception.get_errors()), 1)

    def test_update_client_repository_exception(self):
        with self.assertRaises(RepositoryException):
            self.__client_services.update_client(14, "aaa")

    def test_update_client(self):
        self.__client_services.add_client(14, "aaa")
        self.__client_services.update_client(14, "vvv")
        self.assertEqual(self.__client_services.search_clients_by_name("vvv"), [Client(14, "vvv")])

    def test_search_client_by_id_none(self):
        self.assertEqual(self.__client_services.search_client_by_id(14), None)

    def test_search_client_by_id(self):
        self.__client_services.add_client(14, "aaa")
        self.assertEqual(self.__client_services.search_client_by_id(14), Client(14, "aaa"))

    def test_search_clients_by_name(self):
        self.__client_services.add_client(1, "aaa")
        self.__client_services.add_client(3, "aaa")
        clients_list = [Client(1, "aaa"), Client(3, "aaa")]
        self.assertEqual(self.__client_services.search_clients_by_name("aaa"), clients_list)

    def test_get_all_clients(self):
        clients = self.__client_services.get_all_clients()
        self.assertEqual(len(clients), 0)

    def tearDown(self) -> None:
        pass


class MovieServicesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__client_repository = ClientRepository()
        self.__movie_repository = MovieRepository()
        self.__rental_repository = RentalRepository()
        self.__undo_redo_services = UndoRedoServices()
        self.__rental_services = RentalServices(self.__client_repository, self.__movie_repository, self.__rental_repository, self.__undo_redo_services)
        self.__movie_services = MovieServices(self.__movie_repository, self.__rental_services, self.__undo_redo_services)

    def test_add_movie_exception(self):
        try:
            self.__movie_services.add_movie(1, "", "movie's description", "drama")
            assert False
        except ValidatorException as exception:
            self.assertEqual(len(exception.get_errors()), 1)

    def test_add_movie_repository_exception(self):
        self.__movie_repository.add(Movie(1, "titanic", "description", "drama"))
        with self.assertRaises(RepositoryException):
            self.__movie_services.add_movie(1, "the godfather", "description", "action")

    def test_add_movie(self):
        self.__movie_services.add_movie(1, "titanic", "description", "drama")
        movies = self.__movie_services.get_all_movies()
        self.assertEqual(len(movies), 1)

    def test_remove_movie_exception(self):
        try:
            self.__movie_services.remove_movie(-1)
            assert False
        except ValidatorException as exception:
            self.assertEqual(len(exception.get_errors()), 1)

    def test_remove_movie_repository_exception(self):
        with self.assertRaises(RepositoryException):
            self.__movie_services.remove_movie(1)

    def test_remove_movie(self):
        self.__movie_services.add_movie(1, "titanic", "description", "drama")
        self.__movie_services.remove_movie(1)
        clients = self.__movie_services.get_all_movies()
        self.assertEqual(len(clients), 0)

    def test_update_movie_exception(self):
        try:
            self.__movie_services.update_movie(1, "", "description", "drama")
            assert False
        except ValidatorException as exception:
            self.assertEqual(len(exception.get_errors()), 1)

    def test_update_movie_repository_exception(self):
        with self.assertRaises(RepositoryException):
            self.__movie_services.update_movie(1, "titanic", "description", "drama")

    def test_update_movie(self):
        self.__movie_services.add_movie(1, "titanic", "titanic's description", "drama")
        self.__movie_services.update_movie(1, "the godfather", "the godfather movie's description", "action")
        updated_movie = Movie(1, "the godfather", "the godfather movie's description", "action")
        self.assertEqual(self.__movie_services.search_movies_by_title("the godfather"), [updated_movie])

    def test_search_movie_by_id_None(self):
        self.assertEqual(self.__movie_services.search_movie_by_id(14), None)

    def test_search_movie_by_id(self):
        self.__movie_services.add_movie(1, "titanic", "titanic's description", "drama")
        movie_found = Movie(1, "titanic", "titanic's description", "drama")
        self.assertEqual(self.__movie_services.search_movie_by_id(1), movie_found)

    def test_search_movies_by_title_no_result(self):
        self.assertEqual(self.__movie_services.search_movies_by_title("titanic"), [])

    def test_search_movies_by_title(self):
        self.__movie_services.add_movie(1, "titanic", "titanic's description", "drama")
        self.__movie_services.add_movie(2, "titanic", "movie's description", "history")
        movies_list = [Movie(1, "titanic", "titanic's description", "drama"), Movie(2, "titanic", "movie's description", "history")]
        self.assertEqual(self.__movie_services.search_movies_by_title("titanic"), movies_list)

    def test_search_movies_by_description_no_result(self):
        self.assertEqual(self.__movie_services.search_movies_by_description("movie's description"), [])

    def test_search_movies_by_description(self):
        self.__movie_services.add_movie(1, "titanic", "movie's description", "drama")
        self.__movie_services.add_movie(2, "the godfather", "movie's description", "action")
        movies_list = [Movie(1, "titanic", "movie's description", "drama"), Movie(2, "the godfather", "movie's description", "action")]
        self.assertEqual(self.__movie_services.search_movies_by_description("movie's description"), movies_list)

    def test_search_movies_by_genre_no_result(self):
        self.assertEqual(self.__movie_services.search_movies_by_title("action"), [])

    def test_search_movies_by_genre(self):
        self.__movie_services.add_movie(1, "titanic", "titanic movie's description", "drama")
        self.__movie_services.add_movie(2, "the godfather", "the godfather movie's description", "drama")
        movies_list = [Movie(1, "titanic", "titanic movie's description", "drama"), Movie(2, "the godfather", "the godfather movie's description", "drama")]
        self.assertEqual(self.__movie_services.search_movies_by_genre("drama"), movies_list)

    def test_get_all_movies(self):
        clients = self.__movie_services.get_all_movies()
        self.assertEqual(len(clients), 0)

    def tearDown(self) -> None:
        pass


class RentalServicesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__client_repository = ClientRepository()
        self.__movie_repository = MovieRepository()
        self.__rental_repository = RentalRepository()
        self.__undo_redo_services = UndoRedoServices()
        self.__rental_services = RentalServices(self.__client_repository, self.__movie_repository, self.__rental_repository, self.__undo_redo_services)

    def test_add_rental_exception(self):
        first_client = Client(1, "aaa")
        self.__client_repository.add(first_client)

        first_movie = Movie(1, "titanic", "description", "drama")
        self.__movie_repository.add(first_movie)

        first_rental = Rental(1, 1, 1, "2021-02-03", "2021-05-02", "2021-04-08")
        self.__rental_repository.add(first_rental)

        second_client = Client(2, "Sett")
        self.__client_repository.add(second_client)

        second_movie = Movie(2, "the godfather", "the godfather movie's description", "drama")
        self.__movie_repository.add(second_movie)

        second_rental = Rental(1, 2, 2, "2021-02-03", "2021-05-02", "2021-05-01")

        with self.assertRaises(RepositoryException):
            self.__rental_services.add_rental(second_rental)

    def test_add_rental(self):
        first_client = Client(1, "aaa")
        self.__client_repository.add(first_client)
        second_client = Client(2, "bbb")
        self.__client_repository.add(second_client)

        first_movie = Movie(1, "titanic", "description", "drama")
        self.__movie_repository.add(first_movie)
        second_movie = Movie(2, "the godfather", "description", "drama")
        self.__movie_repository.add(second_movie)

        first_rental = Rental(1, 1, 1, "2021-02-03", "2021-05-02", "2021-04-08")
        self.__rental_services.add_rental(first_rental)
        second_rental = Rental(5, 2, 2, "2021-02-03", "2021-05-02", "2021-05-01")
        self.__rental_services.add_rental(second_rental)

        self.assertEqual(len(self.__rental_services.get_all_rentals()), 2)

    def test_remove_rentals_client_id(self):
        first_client = Client(1, "aaa")
        self.__client_repository.add(first_client)

        first_movie = Movie(1, "titanic", "description", "drama")
        self.__movie_repository.add(first_movie)
        second_movie = Movie(2, "the godfather", "description", "drama")
        self.__movie_repository.add(second_movie)

        first_rental = Rental(1, 1, 1, "2021-02-03", "2021-05-02", "2021-04-08")
        self.__rental_services.add_rental(first_rental)
        second_rental = Rental(5, 2, 1, "2021-02-03", "2021-05-02", "2021-05-01")
        self.__rental_services.add_rental(second_rental)

        self.__rental_services.remove_rentals_client_id(1)

        self.assertEqual(len(self.__rental_services.get_all_rentals()), 0)

    def test_remove_rentals_movie_id(self):
        first_client = Client(1, "aaa")
        self.__client_repository.add(first_client)
        second_client = Client(2, "bbb")
        self.__client_repository.add(second_client)

        first_movie = Movie(1, "titanic", "description", "drama")
        self.__movie_repository.add(first_movie)

        first_rental = Rental(1, 1, 1, "2021-02-03", "2021-05-02", "2021-04-08")
        self.__rental_services.add_rental(first_rental)
        second_rental = Rental(5, 1, 2, "2021-02-03", "2021-05-02", "2021-05-01")
        self.__rental_services.add_rental(second_rental)

        self.__rental_services.remove_rentals_movie_id(1)

        self.assertEqual(len(self.__rental_services.get_all_rentals()), 0)

    def test_rent_new_movie(self):
        client = Client(1, "aaa")
        self.__client_repository.add(client)

        movie = Movie(1, "titanic", " description", "drama")
        self.__movie_repository.add(movie)

        self.__rental_services.rent_new_movie(1, 1, 1, "2021-02-03")
        self.assertEqual(self.__rental_services.get_all_rentals_dto()[0].__str__(), '1 - aaa - titanic - 2021-02-03 - 2021-05-04 - "n/a"')

    def test_return_movie(self):
        client = Client(1, "aaa")
        self.__client_repository.add(client)

        movie = Movie(1, "titanic", "description", "drama")
        self.__movie_repository.add(movie)

        self.__rental_services.rent_new_movie(1, 1, 1, "2021-02-03")

        self.__rental_services.return_a_movie(1, "2022-01-01")

        self.assertEqual(self.__rental_services.get_all_rentals_dto()[0].__str__(), '1 - aaa - titanic - 2021-02-03 - 2021-05-04 - 2022-01-01')

    def test_return_movie_exception(self):
        with self.assertRaises(RepositoryException):
            self.__rental_services.return_a_movie(2, "2022-01-01")

    def test_get_late_rentals_empty_list(self):
        first_client = Client(1, "aaa")
        self.__client_repository.add(first_client)
        second_client = Client(2, "bbb")
        self.__client_repository.add(second_client)

        first_movie = Movie(1, "titanic", "description", "drama")
        self.__movie_repository.add(first_movie)
        second_movie = Movie(2, "the godfather", "description", "drama")
        self.__movie_repository.add(second_movie)

        first_rental = Rental(1, 1, 1, "2021-02-03", "2021-05-02", "2021-04-08")
        self.__rental_repository.add(first_rental)
        second_rental = Rental(5, 2, 2, "2021-02-03", "2021-05-02", "2021-05-01")
        self.__rental_repository.add(second_rental)

        self.assertEqual(self.__rental_services.get_late_rentals_descending_order(), [])

    def test_get_all_rentals_one_rental(self):
        client = Client(1, "aaa")
        self.__client_repository.add(client)
        movie = Movie(1, "titanic", "description", "drama")
        self.__movie_repository.add(movie)
        rental = Rental(1, 1, 1, "2021-02-03", "2021-05-02", '"n/a"')
        self.__rental_repository.add(rental)

        rentals = self.__rental_services.get_all_rentals_dto()
        added_rental = rentals[0]

        self.assertEqual(added_rental.__str__(), '1 - aaa - titanic - 2021-02-03 - 2021-05-02 - "n/a"')

    def test_get_all_rentals_empty_list(self):
        self.assertEqual(self.__rental_services.get_all_rentals_dto(), [])

    def tearDown(self) -> None:
        pass
