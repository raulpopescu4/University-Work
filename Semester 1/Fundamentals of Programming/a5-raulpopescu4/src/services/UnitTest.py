from src.ui.UI import ExpenseUI
from src.domain.Expense import Expense
from src.services.ExpenseService import ExpenseService


class UnitTest:
    def __init__(self):
        self.__expense_service = ExpenseService()
        self.__expense_ui = ExpenseUI()

    def test_all(self):
        self.__expense_service.generate_test_list()
        self.test_expense_class()
        self.test_add_expense()
        self.test_create_expense()
        self.__expense_service.add_to_expense_list_history()
        self.test_filter()
        self.test_undo()

    @staticmethod
    def test_expense_class():
        expense = Expense(3, 21, 'others')
        assert(expense.day == 3)
        assert(expense.amount == 21)
        assert(expense.expense_type == 'others')

    def test_add_expense(self):
        self.__expense_service.add_expense(Expense(3, 4, 'housekeeping'))
        self.__expense_service.add_expense(Expense(4, 623, 'others'))

        assert(len(self.__expense_service.expense_list) == 12)

    def test_create_expense(self):
        expense = self.__expense_service.create_expense(3, 4, 'housekeeping')
        assert (expense.day == 3)
        assert (expense.amount == 4)
        assert (expense.expense_type == 'housekeeping')

    def test_filter(self):
        self.__expense_service.filter_expense_list_by_amount(100)
        expense_list = self.__expense_service.expense_list
        assert(len(expense_list) == 6)

    def test_undo(self):
        self.__expense_service.undo()
        assert (len(self.__expense_service.expense_list) == 12)




