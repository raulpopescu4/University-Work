from src.repository.client_repository import ClientRepository
from src.repository.movie_repository import MovieRepository
from src.repository.rental_repository import RentalRepository
from src.services.client_services import ClientServices
from src.services.movie_services import MovieServices
from src.services.rental_services import RentalServices
from src.ui.ui import UI
from src.services.undo_redo_services import UndoRedoServices

client_repository = ClientRepository()
movie_repository = MovieRepository()
rental_repository = RentalRepository()
undo_redo_services = UndoRedoServices()

rental_services = RentalServices(client_repository, movie_repository, rental_repository, undo_redo_services)
movie_services = MovieServices(movie_repository, rental_services, undo_redo_services)
client_services = ClientServices(client_repository, rental_services, undo_redo_services)

ui = UI(client_services, movie_services, rental_services, undo_redo_services)

ui.run_program()