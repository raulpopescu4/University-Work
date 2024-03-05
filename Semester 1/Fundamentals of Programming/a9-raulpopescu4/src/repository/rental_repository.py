from src.exceptions_and_validators.exceptions import RepositoryException
import pickle

class RentalRepository:
    def __init__(self):
        self._rental_repository = dict()

    def search(self, rental_id):
        if rental_id not in self._rental_repository:
            raise RepositoryException("Rental ID does not exist!")
        return self._rental_repository[rental_id]

    def add(self, rental):
        if rental.get_id() in self._rental_repository:
            raise RepositoryException("Rental ID already existing!")
        self._rental_repository[rental.get_id()] = rental

    def update(self, rental):
        if rental.get_id() not in self._rental_repository:
            raise RepositoryException("Rental ID does not exist!")
        self._rental_repository[rental.get_id()] = rental

    def remove(self, rental_id):
        if rental_id not in self._rental_repository:
            raise RepositoryException("Rental ID does not exist!")
        del self._rental_repository[rental_id]

    def get_all(self):
        return self._rental_repository.values()

    def __len__(self):
        return len(self._rental_repository)


class RentalTextFileRepository(RentalRepository):
    def __init__(self, file_path, entity_from_line, entity_to_line):
        super().__init__()
        self.__file_path = file_path
        self.__entity_from_line = entity_from_line
        self.__entity_to_line = entity_to_line

    def __append_to_file(self, entity):
        with open(self.__file_path, 'a') as f:
            f.write(self.__entity_to_line(entity) + '\n')

    def __read_from_file(self):
        with open(self.__file_path, 'r') as f:
            lines = f.readlines()
            self._rental_repository.clear()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    entity = self.__entity_from_line(line)
                    self._rental_repository[entity.get_id()] = entity

    def __write_to_file(self):
        with open(self.__file_path, 'w') as f:
            for entity_id in self._rental_repository:
                f.write(self.__entity_to_line(self._rental_repository[entity_id]) + '\n')

    def add(self, entity):
        self.__read_from_file()
        super().add(entity)
        self.__append_to_file(entity)

    def search(self, entity_id):
        self.__read_from_file()
        return super().search(entity_id)

    def remove(self, entity_id):
        self.__read_from_file()
        super().remove(entity_id)
        self.__write_to_file()

    def update(self, entity):
        self.__read_from_file()
        super().update(entity)
        self.__write_to_file()

    def get_all(self):
        self.__read_from_file()
        return super().get_all()

    def __len__(self):
        self.__read_from_file()
        return super().__len__()


class RentalPickleRepository(RentalRepository):
    def __init__(self, file_path):
        super().__init__()
        self.__file_path = file_path

    def __read_from_file(self):
        with open(self.__file_path, 'rb') as f:
            try:
                self._rental_repository = pickle.load(f)
            except EOFError:
                pass

    def __write_to_file(self):
        with open(self.__file_path, 'wb') as file:
            pickle.dump(self._rental_repository, file)

    def __append_to_file(self):
        with open(self.__file_path, 'wb') as file:
            pickle.dump(self._rental_repository, file)

    def add(self, entity):
        self.__read_from_file()
        super().add(entity)
        self.__append_to_file()

    def search(self, entity_id):
        self.__read_from_file()
        return super().search(entity_id)

    def remove(self, entity_id):
        self.__read_from_file()
        super().remove(entity_id)
        self.__write_to_file()

    def update(self, entity):
        self.__read_from_file()
        super().update(entity)
        self.__write_to_file()

    def get_all(self):
        self.__read_from_file()
        return super().get_all()

    def __len__(self):
        self.__read_from_file()
        return super().__len__()

