import copy

from src.domain.movie import Movie
from src.exceptions_and_validators.validators import MovieValidator
from src.services.undo_redo_services import Call, Operation, ComplexOperation

class MovieServices:
    def __init__(self, movie_repository, rental_services, undo_redo_services):
        self._movie_repository = movie_repository
        self.__rental_services = rental_services
        self.__undo_redo_services = undo_redo_services

    def generate_movies_data(self):
        """Create 20 procedurally generated movies in the application at startup."""
        self._movie_repository.add(Movie(11, "aaa", "vvv", "drama"))
        self._movie_repository.add(Movie(31, "sss", "vvv", "drama"))
        self._movie_repository.add(Movie(24, "ddd", "vvv", "drama"))
        self._movie_repository.add(Movie(23, "eee", "vvv", "action"))
        self._movie_repository.add(Movie(15, "ggg", "vvv", "comedy"))
        self._movie_repository.add(Movie(7, "hh", "vvv", "comedy"))
        self._movie_repository.add(Movie(99, "fff", "vvv", "drama"))
        self._movie_repository.add(Movie(65, "jjj", "vvv", "comedy"))
        self._movie_repository.add(Movie(45, "ooo", "vvv", "comedy"))
        self._movie_repository.add(Movie(27, "ppp", "vvv", "comedy"))
        self._movie_repository.add(Movie(98, "iii", "vvv", "action"))
        self._movie_repository.add(Movie(21, "eee", "vvv", "comedy"))
        self._movie_repository.add(Movie(49, "www", "vvv", "drama"))
        self._movie_repository.add(Movie(82, "qqq", "vvv", "comedy"))
        self._movie_repository.add(Movie(70, "mmm", "vvv", "action"))
        self._movie_repository.add(Movie(36, "nnn", "vvv", "comedy"))
        self._movie_repository.add(Movie(2, "zzz", "vvv", "comedy"))
        self._movie_repository.add(Movie(5, "bbb", "vvv", "comedy"))
        self._movie_repository.add(Movie(76, "yyy", "vvv", "drama"))
        self._movie_repository.add(Movie(34, "lll", "vvv", "action"))

    def add_movie(self, movie_id, movie_title, movie_description, movie_genre):
        """
        Add a new movie to the movie data list, by creating a new instance of the Movie class and passing
        it to the add function from the Repository class.
        :param movie_id:
        :param movie_title:
        :param movie_description:
        :param movie_genre:
        """
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        MovieValidator.validate(movie)
        self._movie_repository.add(movie)

        undo_call = Call(self._movie_repository.remove, movie_id)
        redo_call = Call(self._movie_repository.add, movie)

        self.__undo_redo_services.record(Operation(undo_call, redo_call))

    def remove_movie(self, movie_id):
        """
        Remove an existing movie from the movie data list, by creating a new instance of the Movie class with the
        given id and passing it to the remove function from the Repository class.
        :param movie_id:
        """
        movie = Movie(movie_id, "test", "test", "test")
        MovieValidator.validate(movie)

        movie_removed = self._movie_repository.search(movie_id)
        self._movie_repository.remove(movie_id)

        undo_call = Call(self._movie_repository.add, movie_removed)
        redo_call = Call(self._movie_repository.remove, movie_id)

        undo_redo_operations = list()
        undo_redo_operations.append(Operation(undo_call, redo_call))

        rentals = self.__rental_services.get_all_rentals()
        for rental in rentals:
            if movie.get_id() == movie_id:
                redo_call = Call(self.__rental_services.remove_rentals_movie_id, movie_id)
                undo_call = Call(self.__rental_services.add_rental, rental)
                undo_redo_operations.append(Operation(undo_call, redo_call))

        self.__undo_redo_services.record(ComplexOperation(undo_redo_operations))
        self.__rental_services.remove_rentals_movie_id(movie_id)

    def update_movie(self, movie_id, movie_title, movie_description, movie_genre):
        """
        Update an existing movie to the movie data list, by creating a new instance of the Movie class with the
        new given data and passing it to the update function from the Repository class.
        :param movie_id:
        :param movie_title:
        :param movie_description:
        :param movie_genre:
        """
        movie = Movie(movie_id, movie_title, movie_description, movie_genre)
        MovieValidator.validate(movie)

        movie_before_update = copy.deepcopy(self._movie_repository.search(movie_id))
        self._movie_repository.update(movie)

        undo_call = Call(self._movie_repository.update, movie_before_update)
        redo_call = Call(self._movie_repository.update, movie)

        self.__undo_redo_services.record(Operation(undo_call, redo_call))

    def search_movie_by_id(self, movie_id):
        """
        Given the id of a movie, search through the repository and find if there exists a movie with this id.
        :param movie_id:
        :return:
        """
        movies = self._movie_repository.get_all()
        for movie in movies:
            if movie.get_id() == movie_id:
                return movie
        return None

    def search_movies_by_title(self, movie_title):
        """
        Given the title of a movie, search through the repository and find if there exist movies with this title.
        The search will be case-insensitive, partial string matching.
        :param movie_title:
        :return:
        """
        movies = self._movie_repository.get_all()
        movies_with_given_name = list()
        for movie in movies:
            if movie.get_title().lower() == movie_title.lower() or movie_title.lower() in movie.get_title().lower():
                movies_with_given_name.append(movie)
        return movies_with_given_name

    def search_movies_by_description(self, movie_description):
        """
        Given the description of a movie, search through the repository and find if there exist movies with this
        description.
        The search will be case-insensitive, partial string matching.
        :param movie_description:
        :return:
        """
        movies = self._movie_repository.get_all()
        movies_with_given_description = list()
        for movie in movies:
            if movie.get_description().lower() == movie_description.lower() or movie_description.lower() in movie.get_description().lower():
                movies_with_given_description.append(movie)
        return movies_with_given_description

    def search_movies_by_genre(self, movie_genre):
        """
        Given the genre of a movie, search through the repository and find if there exist movies with this genre.
        The search will be case-insensitive, partial string matching.
        :param movie_genre:
        :return:
        """
        movies = self._movie_repository.get_all()
        movies_with_given_genre = list()
        for movie in movies:
            if movie.get_genre().lower() == movie_genre.lower() or movie_genre.lower() in movie.get_genre().lower():
                movies_with_given_genre.append(movie)
        return movies_with_given_genre

    def get_all_movies(self):
        """
        Get all the data about movies from the Repository class.
        :return:
        """
        return self._movie_repository.get_all()
