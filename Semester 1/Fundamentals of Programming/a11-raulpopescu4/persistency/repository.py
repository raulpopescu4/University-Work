from validators_and_exceptions import RepositoryException


class Repository:
    def __init__(self):
        self._entities = list()

    def add(self, entity):
        if entity in self._entities:
            raise RepositoryException("Entity already exists")
        self._entities.append(entity)

    def get_all(self):
        return self._entities[:]

    def search(self, entity):
        if entity not in self._entities:
            raise RepositoryException("Nonexistent entity")

        for ent in self._entities:
            if ent == entity:
                return ent


