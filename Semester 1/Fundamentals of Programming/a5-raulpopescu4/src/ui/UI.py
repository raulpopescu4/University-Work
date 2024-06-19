from src.services.ExpenseService import ExpenseService


class ExpenseUI:
    def __init__(self):
        self.__expense_service = ExpenseService()

    def start_menu(self):

        self.print_welcome_message()
        self.__expense_service.generate_start_expense_list()
        self.__expense_service.sort_expense_list_day()

        while True:
            self.show_start_commands()
            user_option = input("Enter an option: ")
            print()
            try:
                if user_option == '1':
                    self.__expense_service.add_to_expense_list_history()
                    self.ui_add_expense()
                    self.__expense_service.sort_expense_list_day()

                elif user_option == '2':
                    self.list_expense_list()

                elif user_option == '3':
                    self.__expense_service.add_to_expense_list_history()
                    self.ui_filter_list()
                    self.__expense_service.sort_expense_list_day()

                elif user_option == '4':
                    self.ui_undo()

                elif user_option == '5':
                    break

                else:
                    print("Option does not exist. Choose an integer number between 1 and 5.\n")

            except ValueError as ve:
                print(ve)

    @staticmethod
    def print_welcome_message():
        print("Welcome to your expenses list manager! Choose one of the options below.\n")

    @staticmethod
    def show_start_commands():
        print("1. Add an expense. You need to provide a day, an amount and a type.")
        print("2. Display the list of expenses.")
        print("3. Filter the list so that it contains only expenses above a certain value you provide.")
        print("4. Undo the last operation that modified the program data.")
        print("5. Exit the program.\n")

    @staticmethod
    def get_day_input():
        while True:
            try:
                user_input = int(input("Please enter the day in which the expense was made: "))
                break
            except ValueError as ve:
                print(ve, "The input must be an integer")
        return user_input

    @staticmethod
    def get_amount_input():
        while True:
            try:
                user_input = int(input("Please enter the amount of the expense that was made: "))
                break
            except ValueError as ve:
                print(ve, "The input must be an integer")
        return user_input

    @staticmethod
    def get_expense_type_input():
        user_input = int(input("Please enter the expense type of the expense that was made: "))
        return user_input

    def ui_create_expense(self):
        print("In order to add an expense to the list, you need to provide a day number, an amount and a type.")

        day = self.get_day_input()
        amount = self.get_amount_input()
        expense_type = self.get_expense_type_input()

        new_expense = self.__expense_service.create_expense(day, amount, expense_type)
        return new_expense

    def ui_add_expense(self):
        self.__expense_service.add_expense(self.ui_create_expense())
        print("\nThe expense has been successfully added!\n")

    def list_expense_list(self):
        expense_list = self.__expense_service.expense_list
        print("The list of the expenses made:\n")

        for expense in expense_list:
            print(f"Day {expense.day} {expense.amount} {expense.expense_type}")
        print()

    @staticmethod
    def get_amount_filter():
        print("Enter a value and the expense list will be filtered "
              "so it will contain only expenses above the entered value.")

        while True:
            try:
                user_input = int(input("Enter the value: "))
                break
            except ValueError as ve:
                print(ve, "The value you enter must be an integer")
        return user_input

    def ui_filter_list(self):
        amount = self.get_amount_input()
        self.__expense_service.filter_expense_list_by_amount(amount)
        print("\nThe expense list has been successfully filtered!\n")

    def ui_undo(self):
        self.__expense_service.undo()
        print("The last operation performed has been successfully undone!\n")
