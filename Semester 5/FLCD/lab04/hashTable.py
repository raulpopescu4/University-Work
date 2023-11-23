class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def valid(self):
        return self.key != -1 and self.value != -1


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def hash_function(self, key):
        total_sum = sum(ord(char) for char in key)
        return total_sum % self.size

    def get_element(self, position):
        try:
            if len(self.table) <= position.key or len(self.table[position.key]) <= position.value:
                raise IndexError("Invalid position")
            return self.table[position.key][position.value]
        except IndexError as e:
            print(e)

    def search(self, element):
        row_number = self.hash_function(element)
        searched_position = (-1, -1)

        row = self.table[row_number]
        if not row:
            return searched_position

        for index, value in enumerate(row):
            if value == element:
                searched_position = (row_number, index)
                break

        return searched_position

    def add(self, element):
        element_position = self.search(element)

        if element_position != (-1, -1):
            return element_position

        row_number = self.hash_function(element)
        row = self.table[row_number]

        row.append(element)
        index = row.index(element)

        element_position = (row_number, index)

        return element_position

    def remove(self, element):
        element_position = self.search(element)

        if element_position != (-1, -1):
            self.table[element_position[0]].remove(element)
        else:
            raise ValueError(f"Element not found: {element}")

    def __str__(self):
        return f"Table: {self.table}"
