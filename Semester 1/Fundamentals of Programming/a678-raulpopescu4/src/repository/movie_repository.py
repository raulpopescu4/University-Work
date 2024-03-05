from src.exceptions_and_validators.exceptions import RepositoryException


class MovieRepository:
    def __init__(self):
        self.__movie_repository = dict()

    def search(self, movie_id):
        if movie_id not in self.__movie_repository:
            raise RepositoryException("Movie ID does not exist!")
        return self.__movie_repository[movie_id]

    def add(self, movie):
        if movie.get_id() in self.__movie_repository:
            raise RepositoryException("Movie ID already existing!")
        self.__movie_repository[movie.get_id()] = movie

    def update(self, movie):
        if movie.get_id() not in self.__movie_repository:
            raise RepositoryException("Movie ID does not exist!")
        self.__movie_repository[movie.get_id()] = movie

    def remove(self, movie_id):
        if movie_id not in self.__movie_repository:
            raise RepositoryException("Movie ID does not exist!")
        del self.__movie_repository[movie_id]

    def get_all(self):
        return self.__movie_repository.values()

    def __len__(self):
        return len(self.__movie_repository)
