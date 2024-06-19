from src.domain.Expense import Expense
import random
import copy


class ExpenseService:

    def __init__(self):
        self.__expense_list = []
        self.__expense_list_history = []

    @property
    def expense_list(self):
        """
        Returns the list of expenses
        :return:
        """
        return self.__expense_list

    def add_expense(self, expense):
        """
        Adds a new expense to the expense list
        :param expense:
        :return:
        """
        if 1 > expense.day > 31:
            raise ValueError("\n The day must be between 1 and 31 !!! \n")
        if expense.amount < 0:
            raise ValueError("\n The amount must be a positive value !!! \n")
        if expense.expense_type not in ["housekeeping", "food", "transport", "clothing", "internet", "others"]:
            raise ValueError("\n The expense type must be one of the following: housekeeping, transport, clothing,"
                             "internet, others")

        self.__expense_list.append(expense)

    def generate_start_expense_list(self):
        """
        Generates a random expense list for the start of the program
        :return:
        """
        expense_types = ['housekeeping', 'food', 'transport', 'clothing', 'internet', 'others']

        for expense in range(1, 16):
            day = random.randint(1, 31)
            amount = random.randint(1, 1000)
            expense_type = random.choice(expense_types)
            self.add_expense(Expense(day, amount, expense_type))

    def generate_test_list(self):
        """
        Creates an expense list used for tests
        :return:
        """
        self.add_expense(Expense(1, 175, "food"))
        self.add_expense(Expense(4, 200, "others"))
        self.add_expense(Expense(8, 10, "transport"))
        self.add_expense(Expense(10, 44, "housekeeping"))
        self.add_expense(Expense(14, 231, "food"))
        self.add_expense(Expense(15, 10, "others"))
        self.add_expense(Expense(19, 155, "clothing"))
        self.add_expense(Expense(22, 35, "transport"))
        self.add_expense(Expense(27, 20, "internet"))
        self.add_expense(Expense(27, 500, "housekeeping"))

        return self.__expense_list

    @staticmethod
    def create_expense(day, amount, expense_type):
        """
        Creates a new expense entity
        :param day:
        :param amount:
        :param expense_type:
        :return:
        """
        return Expense(day, amount, expense_type)

    def sort_expense_list_day(self):
        """
        This function sorts the expense list by the day
        :return:
        """
        for i in range(1, len(self.__expense_list)):
            current_day = self.__expense_list[i].day
            pos = i
            current_expense = self.__expense_list[i]
            while pos > 0 and self.__expense_list[pos - 1].day > current_day:
                self.__expense_list[pos] = self.__expense_list[pos - 1]
                pos -= 1

            self.__expense_list[pos] = current_expense

    def add_to_expense_list_history(self):
        """
        Adds the version of the list to the history of expense lists
        :return:
        """
        copy_expense_list = copy.deepcopy(self.__expense_list)
        self.__expense_list_history.append(copy_expense_list)

    def undo(self):
        """
        This function switches to the version before  in the history of expense lists and makes the operation of undo
        :return:
        """
        if len(self.__expense_list_history) == 0:
            raise ValueError("\nThere are no more operations to be undone\n")

        previous_expense_list = copy.deepcopy(self.__expense_list_history[-1])
        self.__expense_list = previous_expense_list

        self.__expense_list_history.pop()

    def filter_expense_list_by_amount(self, amount):
        """
        Deletes all the expenses with the amount value smaller than the given one.
        :param amount:
        :return:
        """
        if amount < 0:
            raise ValueError("\n The amount for the filter must be positive")

        i = 0
        while i < len(self.__expense_list):
            if self.__expense_list[i].amount < amount:
                del self.__expense_list[i]
                i -= 1
            i += 1
