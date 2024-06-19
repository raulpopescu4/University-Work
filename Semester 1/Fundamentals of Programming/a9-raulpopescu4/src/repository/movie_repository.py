from src.exceptions_and_validators.exceptions import RepositoryException
import pickle

class MovieRepository:
    def __init__(self):
        self._movie_repository = dict()

    def search(self, movie_id):
        if movie_id not in self._movie_repository:
            raise RepositoryException("Movie ID does not exist!")
        return self._movie_repository[movie_id]

    def add(self, movie):
        if movie.get_id() in self._movie_repository:
            raise RepositoryException("Movie ID already existing!")
        self._movie_repository[movie.get_id()] = movie

    def update(self, movie):
        if movie.get_id() not in self._movie_repository:
            raise RepositoryException("Movie ID does not exist!")
        self._movie_repository[movie.get_id()] = movie

    def remove(self, movie_id):
        if movie_id not in self._movie_repository:
            raise RepositoryException("Movie ID does not exist!")
        del self._movie_repository[movie_id]

    def get_all(self):
        return self._movie_repository.values()

    def __len__(self):
        return len(self._movie_repository)


class MovieTextFileRepository(MovieRepository):
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
            self._movie_repository.clear()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    entity = self.__entity_from_line(line)
                    self._movie_repository[entity.get_id()] = entity

    def __write_to_file(self):
        with open(self.__file_path, 'w') as f:
            for entity_id in self._movie_repository:
                f.write(self.__entity_to_line(self._movie_repository[entity_id]) + '\n')

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


class MoviePickleRepository(MovieRepository):
    def __init__(self, file_path):
        super().__init__()
        self.__file_path = file_path

    def __read_from_file(self):
        with open(self.__file_path, 'rb') as f:
            try:
                self._movie_repository = pickle.load(f)
            except EOFError:
                pass

    def __write_to_file(self):
        with open(self.__file_path, 'wb') as file:
            pickle.dump(self._movie_repository, file)

    def __append_to_file(self):
        with open(self.__file_path, 'wb') as file:
            pickle.dump(self._movie_repository, file)

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