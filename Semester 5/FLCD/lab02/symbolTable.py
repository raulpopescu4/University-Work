from hashTable import HashTable


class SymbolTable:
    def __init__(self, size):
        self.size = size
        self.table = HashTable(size)

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_term(self, position):
        try:
            return self.table.get_element(position)
        except IndexError as e:
            print(e)

    def search(self, term):
        return self.table.search(term)

    def exists(self, term):
        return self.table.search(term).valid()

    def add(self, term):
        return self.table.add(term)

    def remove(self, term):
        try:
            self.table.remove(term)
        except ValueError as e:
            print(e)

    def __str__(self):
        return "Symbol" + str(self.table)
