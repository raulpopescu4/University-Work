from hashTable import HashTable


class SymbolTable:
    def __init__(self, size):
        self.size = size
        self.__table = HashTable(size)

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_term(self, position):
        try:
            return self.__table.get_element(position)
        except IndexError as e:
            print(e)

    def search(self, term):
        return self.__table.search(term)

    def exists(self, term):
        return self.__table.search(term).valid()

    def add(self, term):
        return self.__table.add(term)

    def remove(self, term):
        try:
            self.__table.remove(term)
        except ValueError as e:
            print(e)

    def get_table(self):
        return self.__table

    def __str__(self):
        return "Symbol" + str(self.__table)
