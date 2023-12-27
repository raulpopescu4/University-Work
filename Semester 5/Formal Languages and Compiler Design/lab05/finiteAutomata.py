from transition import Transition


def display_menu():
    print("M = (Q, Σ, d, q0, F)")
    print("[0] Exit the menu.")
    print("[1] Display states.")
    print("[2] Display alphabet.")
    print("[3] Display transitions.")
    print("[4] Display initial state.")
    print("[5] Display final states.")
    print("[6] Display finite automata.")
    print("[7] Check if sequence is accepted.")
    print("Enter your option:")


class FiniteAutomata:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = []
        self.initial_state = ""
        self.final_states = set()
        self.identifier_transitions = []
        self.constant_transitions = []


    def reset_finite_automata(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = []
        self.initial_state = ""
        self.final_states = set()

    def get_states(self):
        return self.states

    def get_alphabet(self):
        return self.alphabet

    def get_transitions(self):
        return self.transitions

    def get_initial_state(self):
        return self.initial_state

    def get_final_states(self):
        return self.final_states

    def set_states(self, states):
        self.states = states

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet

    def set_transitions(self, transitions):
        self.transitions = transitions

    def set_initial_state(self, initial_state):
        self.initial_state = initial_state

    def set_final_states(self, final_states):
        self.final_states = final_states

    def initialize_elements(self, input_file):
        with open(input_file, 'r') as reader:
            line_count = 1

            for line in reader:
                try:
                    self.process_line(line, line_count)
                except ValueError as e:
                    print(f"Error in line {line_count}: {e}")
                    self.reset_finite_automata()
                    break

                line_count += 1

    def process_line(self, line, line_count):
        if line_count == 1:
            self.process_states(line)
        elif line_count == 2:
            self.process_alphabet(line)
        elif line_count == 3:
            self.process_initial_state(line)
        elif line_count == 4:
            self.process_final_states(line)
        elif line_count == 5:
            self.process_transitions(line)
        elif line_count == 6:
            # Add new states and transitions for <identifier> and <integer constant>
            self.add_identifier_transitions()
            self.add_integer_constant_transitions()


    def add_identifier_transitions(self):
        # Add transitions for <identifier>
        for state in self.states:
            self.identifier_transitions.append(Transition(state, 'letter', 'identifier'))
            self.identifier_transitions.append(Transition('identifier', 'letter', 'identifier'))
            self.identifier_transitions.append(Transition('identifier', 'digit', 'identifier'))

    def add_integer_constant_transitions(self):
        # Add transitions for <integer constant>
        for state in self.states:
            self.constant_transitions.append(Transition(state, 'digit', 'integer_constant'))
            self.constant_transitions.append(Transition('integer_constant', 'digit', 'integer_constant'))

    def process_states(self, line):
        start_index = line.find("{") + 1
        end_index = line.find("}")

        if start_index > 0 and end_index > 0:
            state_names = [state.strip() for state in line[start_index:end_index].split(',')]
            self.states.update(state_names)
        else:
            raise ValueError(f"Invalid state format: {line}")

    def process_alphabet(self, line):
        start_index = line.find("{") + 1
        end_index = line.find("}")

        if start_index > 0 and end_index > 0:
            symbols = [char.strip() for char in line[start_index:end_index].split(',')]
            self.alphabet.update(symbols)
        else:
            raise ValueError(f"Invalid alphabet format: {line}")

    def process_initial_state(self, line):
        self.initial_state = line.strip()

    def process_final_states(self, line):
        start_index = line.find("{") + 1
        end_index = line.find("}")

        if start_index > 0 and end_index > 0:
            state_names = [state.strip() for state in line[start_index:end_index].split(',')]
            self.final_states.update(state_names)
        else:
            raise ValueError(f"Invalid final states format: {line}")

    def process_transitions(self, line):
        transition = Transition.from_line(line)
        self.transitions.append(transition)

    def display_states(self):
        print(f"Q = {{{', '.join(self.states)}}}\n")

    def display_alphabet(self):
        print(f"Σ = {{{', '.join(self.alphabet)}}}\n")

    def display_transitions(self):
        for transition in self.transitions:
            print(transition)

    def display_initial_state(self):
        print(f"{self.initial_state}\n")

    def display_final_states(self):
        print(f"F = {{{', '.join(self.final_states)}}}\n")

    def check_if_sequence_is_accepted(self):
        print("Enter the sequence to check:")
        sequence = input()

        is_accepted = self.is_accepted(sequence)
        if is_accepted:
            print("The sequence is accepted by the Finite Automata.\n")
        else:
            print("The sequence is not accepted by the Finite Automata.\n")

    def run_menu(self):
        display_menu()

        option = int(input())
        while option != 0:
            if option == 1:
                self.display_states()
            elif option == 2:
                self.display_alphabet()
            elif option == 3:
                self.display_transitions()
            elif option == 4:
                self.display_initial_state()
            elif option == 5:
                self.display_final_states()
            elif option == 6:
                print(str(self))
            elif option == 7:
                self.check_if_sequence_is_accepted()
            else:
                print("Invalid option. Please enter a valid option.")

            display_menu()
            option = int(input())

        print("Menu closed...")

    def is_dfa(self):
        for state in self.states:
            seen_symbols = set()

            for transition in self.transitions:
                if transition.source_state == state:
                    symbol = transition.input_symbol

                    if symbol in seen_symbols:
                        return False

                    seen_symbols.add(symbol)

            if not seen_symbols.issuperset(self.alphabet):
                return False

        return True

    def is_accepted(self, sequence):
        current_state = self.initial_state

        for symbol in sequence:
            transition_found = False

            for transition in self.transitions:
                if transition.source_state == current_state and transition.input_symbol == symbol:
                    current_state = transition.destination_state
                    transition_found = True
                    break

            if not transition_found:
                return False

        return current_state in self.final_states

    def __str__(self):
        result = []

        result.append(f"Q = {{{', '.join(self.states)}}}")
        result.append(f"Σ = {{{', '.join(self.alphabet)}}}")
        result.append(self.initial_state)
        result.append(f"F = {{{', '.join(self.final_states)}}}")

        for transition in self.transitions:
            result.append(str(transition))

        return '\n'.join(result)
