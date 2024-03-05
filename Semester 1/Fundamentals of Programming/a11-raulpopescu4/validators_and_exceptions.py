class RepositoryException(Exception):
    pass


class ValidationError(Exception):
    pass


class BoardError(Exception):
    pass


class ControllerError(Exception):
    pass


class ShipValidator:
    @staticmethod
    def validate_ship(ship):
        errors = ""
        if ship.get_player() is None:
            errors += "Invalid player !\n"
        if ship.get_length() not in [2, 3, 4, 5]:
            errors += "Invalid length !\n"
        if ship.get_direction() not in [0, 1, 2, 3]:
            errors += "Invalid direction !\n"

        if len(errors) > 0:
            raise ValidationError(errors)

