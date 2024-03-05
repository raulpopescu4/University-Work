from src.exceptions_and_validators.exceptions import RepositoryException


class RentalRepository:
    def __init__(self):
        self.__rental_repository = dict()

    def search(self, rental_id):
        if rental_id not in self.__rental_repository:
            raise RepositoryException("Rental ID does not exist!")
        return self.__rental_repository[rental_id]

    def add(self, rental):
        if rental.get_id() in self.__rental_repository:
            raise RepositoryException("Rental ID already existing!")
        self.__rental_repository[rental.get_id()] = rental

    def update(self, rental):
        if rental.get_id() not in self.__rental_repository:
            raise RepositoryException("Rental ID does not exist!")
        self.__rental_repository[rental.get_id()] = rental

    def remove(self, rental_id):
        if rental_id not in self.__rental_repository:
            raise RepositoryException("Rental ID does not exist!")
        del self.__rental_repository[rental_id]

    def get_all(self):
        return self.__rental_repository.values()

    def __len__(self):
        return len(self.__rental_repository)
