from src.exceptions_and_validators.exceptions import RepositoryException


class ClientRepository:
    def __init__(self):
        self.__client_repository = dict()

    def search(self, client_id):
        if client_id not in self.__client_repository:
            raise RepositoryException("Client ID does not exist!")
        return self.__client_repository[client_id]

    def add(self, client):
        if client.get_id() in self.__client_repository:
            raise RepositoryException("Client ID already existing!")
        self.__client_repository[client.get_id()] = client

    def update(self, client):
        if client.get_id() not in self.__client_repository:
            raise RepositoryException("Client ID does not exist!")
        self.__client_repository[client.get_id()] = client

    def remove(self, client_id):
        if client_id not in self.__client_repository:
            raise RepositoryException("Client ID does not exist!")
        del self.__client_repository[client_id]

    def get_all(self):
        return self.__client_repository.values()

    def __len__(self):
        return len(self.__client_repository)


