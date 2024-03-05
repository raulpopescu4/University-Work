class Expense:
    def __init__(self, day, amount, expense_type):
        self.__day = day
        self.__amount = amount
        self.__expense_type = expense_type

    @property
    def day(self):
        return self.__day

    @property
    def amount(self):
        return self.__amount

    @property
    def expense_type(self):
        return self.__expense_type

    @day.setter
    def day(self, value):
        self.__day = value

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @expense_type.setter
    def expense_type(self, value):
        self.__expense_type = value

