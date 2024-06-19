import copy
import random
import datetime

from src.domain.rental import RentalDTO, Rental, RentalMovieStatisticsDTO, RentalClientStatisticsDTO
from src.exceptions_and_validators.exceptions import RepositoryException
from src.exceptions_and_validators.validators import RentalValidator
from src.services.undo_redo_services import Call, Operation, ComplexOperation


class RentalServices:
    def __init__(self, client_repository, movie_repository, rental_repository, undo_redo_services):
        self.__client_repository = client_repository
        self.__movie_repository = movie_repository
        self.__rental_repository = rental_repository
        self.__undo_redo_services = undo_redo_services

    @staticmethod
    def generate_random_rental_date():
        """
        Generate a random rental date between 2021-07-10 and 2021-11-19.
        :return:
        """
        start_date = datetime.date(2021, 7, 10)
        end_date = datetime.date(2021, 11, 19)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days

        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)

        return random_date

    def generate_random_rental_data(self):
        """Create 20 procedurally generated rentals in the application at startup."""
        rentals_random_ids = list(range(100))

        client_data_list = list(self.__client_repository.get_all())
        movie_data_list = list(self.__movie_repository.get_all())

        for rental_index in range(21):
            random_rental_id = random.choice(rentals_random_ids)
            rentals_random_ids.remove(random_rental_id)

            random_client = random.choice(client_data_list)
            random_client_id = random_client.get_id()

            random_movie = random.choice(movie_data_list)
            random_movie_id = random_movie.get_id()

            random_rental_date = self.generate_random_rental_date()

            due_date = random_rental_date + datetime.timedelta(days=90)

            returned_date = random.choice([random_rental_date + datetime.timedelta(days=random.randint(1, 180)), '"n/a"'])

            rental = Rental(random_rental_id, random_movie_id, random_client_id, random_rental_date, due_date,
                            returned_date)

            self.__rental_repository.add(rental)

    def add_rental(self, rental):
        """
        Add a rental to the repository(it is used only for the undo/redo functionality).
        :param rental:
        """
        self.__rental_repository.add(rental)

    def remove_rentals_client_id(self, client_id):
        """
        Remove all the rentals from the repository for a given client id.
        :param client_id:
        """
        rentals = self.__rental_repository.get_all()
        rental_ids_removed = []

        for rental in rentals:
            rental_client_id = rental.get_client_id()
            if rental_client_id == client_id:
                rental_ids_removed.append(rental.get_id())

        for rental_id in rental_ids_removed:
            self.__rental_repository.remove(rental_id)

    def remove_rentals_movie_id(self, movie_id):
        """
        Remove all the rentals from the repository for a given movie id.
        :param movie_id:
        """
        rentals = self.__rental_repository.get_all()
        rental_ids_removed = []

        for rental in rentals:
            rental_movie_id = rental.get_movie_id()
            if rental_movie_id == movie_id:
                rental_ids_removed.append(rental.get_id())

        for rental_id in rental_ids_removed:
            self.__rental_repository.remove(rental_id)

    def rent_new_movie(self, rental_id, movie_id, client_id, rental_date):
        """
        Rent a new movie for the information provided by the user. A new movie will be added in the repository.
        :param rental_id:
        :param movie_id:
        :param client_id:
        :param rental_date:
        :return:
        """
        test_due_date = str(datetime.date.today())
        rental = Rental(rental_id, movie_id, rental_id, rental_date, test_due_date, '"n/a"')
        RentalValidator.validate(rental)

        try:
            movie = self.__movie_repository.search(movie_id)
        except RepositoryException as exception:
            raise RepositoryException(str(exception))

        try:
            client = self.__client_repository.search(client_id)
        except RepositoryException as exception:
            raise RepositoryException(str(exception))

        client_can_rent = True
        rentals_list = self.__rental_repository.get_all()
        for each_rental in rentals_list:
            if each_rental.get_client_id() == client_id:
                return_date_for_rental = each_rental.get_returned_date() if each_rental.get_returned_date() != '"n/a"' else datetime.date.today()
                due_date_for_rental = datetime.datetime.strptime(str(each_rental.get_due_date()), "%Y-%m-%d")
                if return_date_for_rental > due_date_for_rental.date():
                    client_can_rent = False
                    break

        if client_can_rent is False:
            raise RepositoryException("The client can't rent any more movies!")

        due_date = (datetime.datetime.strptime(rental_date, "%Y-%m-%d") + datetime.timedelta(days=90)).date()

        rental.set_rented_date(datetime.datetime.strptime(rental.get_rented_date(), "%Y-%m-%d").date())
        rental.set_due_date(due_date)

        self.__rental_repository.add(rental)

        undo_call = Call(self.__rental_repository.remove, rental.get_id())
        redo_call = Call(self.__rental_repository.add, rental)

        self.__undo_redo_services.record(Operation(undo_call, redo_call))

    def return_a_movie(self, rental_id, return_date):
        """
        Return a movie with the information provided by the user. An already existing movie's return date will be
        changed with the one given by the user.
        :param rental_id:
        :param return_date:
        :return:
        """
        rental = self.__rental_repository.search(rental_id)

        if rental.get_returned_date() != '"n/a"':
            raise RepositoryException("The movie is already returned!")

        modified_rental = Rental(rental_id, rental.get_movie_id(), rental.get_client_id(),
                                 str(rental.get_rented_date()), str(rental.get_due_date()), return_date)
        RentalValidator.validate(modified_rental)

        modified_rental.set_rented_date(datetime.datetime.strptime(modified_rental.get_rented_date(), "%Y-%m-%d").date())

        modified_rental.set_due_date(datetime.datetime.strptime(modified_rental.get_due_date(), "%Y-%m-%d").date())

        modified_rental.set_returned_date(datetime.datetime.strptime(modified_rental.get_returned_date(), "%Y-%m-%d").date())

        rental_before_return = copy.deepcopy(rental)
        self.__rental_repository.update(modified_rental)

        undo_call = Call(self.__rental_repository.update, rental_before_return)
        redo_call = Call(self.__rental_repository.update, modified_rental)

        self.__undo_redo_services.record(Operation(undo_call, redo_call))

    def get_most_rented_movies(self):
        """
        Get all rentals from repository, see for how long the movies have been rented by any of the users
        and sort them in descending order.
        :return:
        """
        rentals = self.__rental_repository.get_all()
        movie_id_and_days_counter = dict()

        for rental in rentals:
            movie_id = rental.get_movie_id()

            rental_date = rental.get_rented_date()
            return_date = rental.get_returned_date() if rental.get_returned_date() != '"n/a"' else datetime.date.today()

            number_of_rental_days = return_date - rental_date

            if movie_id not in movie_id_and_days_counter:
                movie_id_and_days_counter[movie_id] = 0
            movie_id_and_days_counter[movie_id] += number_of_rental_days.days

        movie_id_and_days_counter = dict(
            sorted(movie_id_and_days_counter.items(), key=lambda item: item[1], reverse=True))
        most_rented_movies_list = list()

        for movie_id in movie_id_and_days_counter:
            movie_title = self.__movie_repository.search(movie_id).get_title()
            number_of_days = movie_id_and_days_counter[movie_id]
            most_rented_movies_list.append(RentalMovieStatisticsDTO(movie_title, number_of_days))

        return most_rented_movies_list[:len(most_rented_movies_list) // 2]

    def get_most_active_clients(self):
        """
        Get all rentals from repository, see how many days the clients have been renting movies, make
        a sum of all of them for each client and sort clients in descending order.
        :return:
        """
        rentals = self.__rental_repository.get_all()
        client_id_and_days_counter = dict()

        for rental in rentals:
            client_id = rental.get_client_id()

            rental_date = rental.get_rented_date()
            return_date = rental.get_returned_date() if rental.get_returned_date() != '"n/a"' else datetime.date.today()

            number_of_rental_days = return_date - rental_date

            if client_id not in client_id_and_days_counter:
                client_id_and_days_counter[client_id] = 0
            client_id_and_days_counter[client_id] += number_of_rental_days.days

        client_id_and_days_counter = dict(
            sorted(client_id_and_days_counter.items(), key=lambda item: item[1], reverse=True))
        most_active_clients_list = list()

        for client_id in client_id_and_days_counter:
            client_name = self.__client_repository.search(client_id).get_name()
            number_of_days = client_id_and_days_counter[client_id]
            most_active_clients_list.append(RentalClientStatisticsDTO(client_name, number_of_days))

        return most_active_clients_list[:len(most_active_clients_list) // 2]

    def get_late_rentals_descending_order(self):
        """
        Get all rentals from repository, see how many days the movies have been rented after they passed the due date,
        check the biggest value for each movie and sort them in descending order.
        :return:
        """
        rentals = self.__rental_repository.get_all()
        movie_id_and_late_days_counter = dict()

        for rental in rentals:
            movie_id = rental.get_movie_id()

            due_date = rental.get_due_date()
            return_date = rental.get_returned_date() if rental.get_returned_date() != '"n/a"' else datetime.date.today()

            if return_date > due_date:
                number_of_late_rental_days = return_date - due_date

                if movie_id not in movie_id_and_late_days_counter:
                    movie_id_and_late_days_counter[movie_id] = number_of_late_rental_days.days
                else:
                    if movie_id_and_late_days_counter[movie_id] < number_of_late_rental_days.days:
                        movie_id_and_late_days_counter[movie_id] = number_of_late_rental_days.days

        movie_id_and_late_days_counter = dict(
            sorted(movie_id_and_late_days_counter.items(), key=lambda item: item[1], reverse=True))
        late_rental_movies_list = list()

        for movie_id in movie_id_and_late_days_counter:
            movie_title = self.__movie_repository.search(movie_id).get_title()
            number_of_days = movie_id_and_late_days_counter[movie_id]
            late_rental_movies_list.append(RentalMovieStatisticsDTO(movie_title, number_of_days))

        return late_rental_movies_list

    def get_all_rentals_dto(self):
        """
        Get all rentals from repository.
        :return:
        """
        rentals = self.__rental_repository.get_all()
        rentals_for_display = list()

        for rental in rentals:
            rental_id = rental.get_id()
            client_id = rental.get_client_id()
            movie_id = rental.get_movie_id()
            client_name = self.__client_repository.search(client_id).get_name()
            movie_title = self.__movie_repository.search(movie_id).get_title()
            rental_date = rental.get_rented_date()
            due_date = rental.get_due_date()
            returned_date = rental.get_returned_date()
            rentals_for_display.append(
                RentalDTO(rental_id, client_name, movie_title, rental_date, due_date, returned_date))

        return rentals_for_display

    def get_all_rentals(self):
        """
        Get all rentals from the repository.
        :return:
        """
        return self.__rental_repository.get_all()
