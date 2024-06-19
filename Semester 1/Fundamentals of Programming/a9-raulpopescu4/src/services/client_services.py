import copy

from src.domain.client import Client
from src.exceptions_and_validators.validators import ClientValidator
from src.services.undo_redo_services import Call, Operation, ComplexOperation


class ClientServices:
    def __init__(self, repository_client, rental_services, undo_redo_services):
        self._client_repository = repository_client
        self.__rental_services = rental_services
        self.__undo_redo_services = undo_redo_services

    def generate_clients_data(self):
        """Create 20 procedurally generated clients in the application at startup."""
        self._client_repository.add(Client(90, "aaa"))
        self._client_repository.add(Client(1, "bbb"))
        self._client_repository.add(Client(17, "ccc"))
        self._client_repository.add(Client(25, "ddd"))
        self._client_repository.add(Client(79, "eee"))
        self._client_repository.add(Client(13, "fff"))
        self._client_repository.add(Client(22, "ggg"))
        self._client_repository.add(Client(5, "hhh"))
        self._client_repository.add(Client(11, "AAA"))
        self._client_repository.add(Client(74, "BBB"))
        self._client_repository.add(Client(65, "CCC"))
        self._client_repository.add(Client(51, "DDD"))
        self._client_repository.add(Client(49, "EEE"))
        self._client_repository.add(Client(42, "FFF"))
        self._client_repository.add(Client(38, "GGG"))
        self._client_repository.add(Client(34, "HHH"))
        self._client_repository.add(Client(27, "zzz"))
        self._client_repository.add(Client(9, "ZZZ"))
        self._client_repository.add(Client(99, "vvv"))
        self._client_repository.add(Client(91, "VVV"))

    def add_client(self, client_id, client_name):
        """
        Add a new client to the client data list, by creating a new instance of the Client class and passing
        it to the add function from the Repository class.
        :param client_id:
        :param client_name:
        """
        client = Client(client_id, client_name)
        ClientValidator.validate(client)
        self._client_repository.add(client)

        undo_call = Call(self._client_repository.remove, client_id)
        redo_call = Call(self._client_repository.add, client)

        self.__undo_redo_services.record(Operation(undo_call, redo_call))

    def remove_client(self, client_id):
        """
        Remove an existing client from the client data list, by creating a new instance of the Client class with the
        given id and passing it to the remove function from the Repository class.
        :param client_id:
        """
        client = Client(client_id, "test")
        ClientValidator.validate(client)

        removed_client = self._client_repository.search(client_id)
        self._client_repository.remove(client_id)

        undo_call = Call(self._client_repository.add, removed_client)
        redo_call = Call(self._client_repository.remove, client_id)

        undo_redo_operations = list()
        undo_redo_operations.append(Operation(undo_call, redo_call))

        rentals = self.__rental_services.get_all_rentals()
        for rental in rentals:
            if rental.get_client_id() == client_id:
                redo_call = Call(self.__rental_services.remove_rentals_client_id, client_id)
                undo_call = Call(self.__rental_services.add_rental, rental)
                undo_redo_operations.append(Operation(undo_call, redo_call))

        self.__undo_redo_services.record(ComplexOperation(undo_redo_operations))
        self.__rental_services.remove_rentals_client_id(client_id)

    def update_client(self, client_id, client_name):
        """
        Update an existing client to the client data list, by creating a new instance of the Client class with the
        new given data and passing it to the update function from the Repository class.
        :param client_id:
        :param client_name:
        """
        client = Client(client_id, client_name)
        ClientValidator.validate(client)

        client_before_update = copy.deepcopy(self._client_repository.search(client_id))
        self._client_repository.update(client)

        undo_call = Call(self._client_repository.update, client_before_update)
        redo_call = Call(self._client_repository.update, client)

        self.__undo_redo_services.record(Operation(undo_call, redo_call))

    def search_client_by_id(self, client_id):
        """
        Given the id of a client, search through the repository and find if there exists a client with this id.
        :param client_id:
        :return:
        """
        clients = self._client_repository.get_all()
        for client in clients:
            if client.get_id() == client_id:
                return client
        return None

    def search_clients_by_name(self, client_name):
        """
        Given the name of a client, search through the repository and find if there exist clients with this name.
        The search will be case-insensitive, partial string matching.
        :param client_name:
        :return:
        """
        clients = self._client_repository.get_all()
        clients_with_given_name = list()
        for client in clients:
            if client.get_name().lower() == client_name.lower() or client_name.lower() in client.get_name().lower():
                clients_with_given_name.append(client)
        return clients_with_given_name

    def get_all_clients(self):
        """
        Get all the data about clients from the Repository class.
        :return:
        """
        return self._client_repository.get_all()
