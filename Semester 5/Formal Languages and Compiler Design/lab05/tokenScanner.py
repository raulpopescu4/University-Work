from finiteAutomata import FiniteAutomata
from transition import Transition


class TokenScanner:
    def __init__(self):
        self.identifier_finite_automata = FiniteAutomata()
        self.initialize_identifier_finite_automata()

        self.integer_constant_finite_automata = FiniteAutomata()
        self.initialize_integer_constant_finite_automata()

    def generate_alphabet_range(self, start, end):
        return set(chr(character) for character in range(ord(start), ord(end) + 1))

    def generate_lower_case_letters(self):
        return self.generate_alphabet_range('a', 'z')

    def generate_upper_case_letters(self):
        return self.generate_alphabet_range('A', 'Z')

    def generate_digits(self):
        return self.generate_alphabet_range('0', '9')

    def generate_nonzero_digits(self):
        return self.generate_alphabet_range('1', '9')

    def generate_transitions_list(self, char_set, source_state, destination_state):
        return [Transition(source_state, element, destination_state) for element in char_set]

    def concatenate_sets(self, set1, set2):
        return set1.union(set2)

    def concatenate_transitions_lists(self, list1, list2):
        return list1 + list2

    def initialize_identifier_finite_automata(self):
        initial_state, final_state = 'q0', 'q1'
        final_states, states = {final_state}, {initial_state, final_state}

        alphabet_q0 = self.concatenate_sets(self.generate_lower_case_letters(),
                                             self.concatenate_sets(self.generate_upper_case_letters(),
                                                                  {'_'}))
        alphabet = self.concatenate_sets(self.generate_digits(), alphabet_q0)

        self.identifier_finite_automata.set_states(states)
        self.identifier_finite_automata.set_alphabet(alphabet)
        self.identifier_finite_automata.set_initial_state(initial_state)
        self.identifier_finite_automata.set_final_states(final_states)

        transitions_q0_q1 = self.generate_transitions_list(alphabet_q0, initial_state, final_state)
        transitions_q1_q1 = self.generate_transitions_list(alphabet, final_state, final_state)

        self.identifier_finite_automata.set_transitions(self.concatenate_transitions_lists(transitions_q0_q1, transitions_q1_q1))

    def initialize_integer_constant_finite_automata(self):
        initial_state, final_state_q2, final_state_q3 = 'q0', 'q2', 'q3'
        final_states, states = {final_state_q2, final_state_q3}, {'q0', 'q1', 'q2', 'q3'}

        digits_alphabet = self.generate_digits()
        nonzero_digits_alphabet = self.generate_nonzero_digits()
        sign_alphabet = {'+', '-'}

        alphabet = self.concatenate_sets(digits_alphabet, sign_alphabet)

        self.integer_constant_finite_automata.set_states(states)
        self.integer_constant_finite_automata.set_alphabet(alphabet)
        self.integer_constant_finite_automata.set_initial_state(initial_state)
        self.integer_constant_finite_automata.set_final_states(final_states)

        transitions_q0_q3 = self.generate_transitions_list({'0'}, initial_state, final_state_q3)
        transitions_q0_q1 = self.generate_transitions_list(sign_alphabet, initial_state, 'q1')
        transitions_q0_q2 = self.generate_transitions_list(nonzero_digits_alphabet, initial_state, final_state_q2)

        transitions_q1_q2 = self.generate_transitions_list(nonzero_digits_alphabet, 'q1', final_state_q2)
        transitions_q2_q2 = self.generate_transitions_list(digits_alphabet, final_state_q2, final_state_q2)

        transitions_q0 = self.concatenate_transitions_lists(transitions_q0_q3,
                                                            self.concatenate_transitions_lists(transitions_q0_q1,
                                                                                               transitions_q0_q2))
        transitions = self.concatenate_transitions_lists(transitions_q0,
                                                         self.concatenate_transitions_lists(transitions_q1_q2,
                                                                                            transitions_q2_q2))

        self.integer_constant_finite_automata.set_transitions(transitions)

    def is_identifier(self, token):
        return self.identifier_finite_automata.is_accepted(token)

    def is_integer_constant(self, token):
        return self.integer_constant_finite_automata.is_accepted(token)
