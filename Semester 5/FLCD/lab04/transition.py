import re

class Transition:
    def __init__(self, source_state, input_symbol, destination_state):
        self.source_state = source_state
        self.input_symbol = input_symbol
        self.destination_state = destination_state

    def get_source_state(self):
        return self.source_state

    def get_input_symbol(self):
        return self.input_symbol

    def get_destination_state(self):
        return self.destination_state

    @staticmethod
    def from_line(line):
        parts = line.split("=")

        if len(parts) == 2:
            left_part = parts[0].strip()
            right_part = parts[1].strip()

            if left_part.startswith("d(") and left_part.endswith(")"):
                inside_delta = left_part[2:-1].split(",")

                if len(inside_delta) == 2:
                    source_state = inside_delta[0].strip()
                    input_symbol = inside_delta[1].strip()[0]
                    destination_state = right_part.strip()

                    return Transition(source_state, input_symbol, destination_state)

        raise ValueError("Invalid transition format: " + line)

    def __str__(self):
        return f"d({self.source_state}, {self.input_symbol}) = {self.destination_state}"
