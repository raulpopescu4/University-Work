from Functions import *


def run_menu_cmd():
    expense_list = initialize_expenses()
    expense_list_history = list()
    while True:
        print_commands_start()
        cmd_line = input()
        words, numbers, operator = get_command_and_args(cmd_line)
        if cmd_line == 'exit':
            break
        try:

            if words[0] == 'add' and len(words) == 2 and len(numbers) == 1 and operator == '':
                add_last_operation_performed(expense_list_history, expense_list)
                ui_add_expense(expense_list, numbers[0], words[1])
            elif words[0] == 'insert' and len(words) == 2 and len(numbers) == 2 and operator == '':
                add_last_operation_performed(expense_list_history, expense_list)
                ui_insert_expense(expense_list, numbers[0], numbers[1], words[1])
            elif words[0] == 'remove':
                if len(words) == 1 and len(numbers) == 1 and operator == '':
                    add_last_operation_performed(expense_list_history, expense_list)
                    ui_remove_expense_day(expense_list, numbers[0])
                elif len(words) == 2 and words[1] == 'to' and len(numbers) == 2 and operator == '':
                    add_last_operation_performed(expense_list_history, expense_list)
                    ui_remove_expense_interval(expense_list, numbers[0], numbers[1])
                elif len(words) == 2 and len(numbers) == 0 and operator == '':
                    add_last_operation_performed(expense_list_history, expense_list)
                    ui_remove_expense_type(expense_list, words[1])
            elif words[0] == 'list':
                if len(words) == 1 and len(numbers) == 0 and operator == '':
                    print_all_expenses(expense_list)
                elif len(words) == 2 and len(numbers) == 0 and operator == '':
                    print_expenses_type(expense_list, words[1])
                elif len(words) == 2 and len(numbers) == 1:
                    if operator == '>':
                        print_expenses_type_greater(expense_list, words[1], numbers[0])
                    elif operator == '=':
                        print_expenses_type_equal(expense_list, words[1], numbers[0])
                    elif operator == '<':
                        print_expenses_type_lower(expense_list, words[1], numbers[0])
            elif words[0] == 'sum' and len(words) == 2 and len(numbers) == 0 and operator == '':
                print_sum_expenses_type(expense_list, words[1])
            elif words[0] == 'max' and words[1] == 'day' and len(words) == 2 and len(numbers) == 0 and operator == '':
                print_max_day_expenses(expense_list)
            elif words[0] == 'sort' and len(words) == 2 and len(numbers) == 0 and operator == '':
                if words[1] == 'day':
                    print_sort_by_amount(expense_list)
                else:
                    print_sort_type(expense_list, words[1])
            elif words[0] == 'filter':
                if len(words) == 2 and len(numbers) == 0 and operator == '':
                    add_last_operation_performed(expense_list_history, expense_list)
                    ui_filter_expense_type(expense_list, words[1])
                elif len(words) == 2 and len(numbers) == 1 and operator != '':
                    if operator == '>':
                        add_last_operation_performed(expense_list_history, expense_list)
                        ui_filter_expense_type_greater(expense_list, words[1], numbers[0])
                    elif operator == '<':
                        add_last_operation_performed(expense_list_history, expense_list)
                        ui_filter_expense_type_lower(expense_list, words[1], numbers[0])
                    elif operator == '=':
                        add_last_operation_performed(expense_list_history, expense_list)
                        ui_filter_expense_type_equal(expense_list, words[1], numbers[0])
            elif words[0] == 'undo' and len(words) == 1 and len(numbers) == 0 and operator == '':
                expense_list = undo(expense_list_history)
            else:
                raise KeyError("The command you inserted is invalid. Please insert one of the following commands !!")




        except ValueError as ve:
            print(str(ve))










def print_all_expenses(expense_list):
    """
    This function prints all the expenses

    :param expense_list:
    :return:
    """

    expense_list = expense_list_sort_day(expense_list)
    for expense in expense_list:
        print(f"Day {get_day(expense)}  {get_amount(expense)}  {get_expense_type(expense)}")


def print_expenses_type(expense_list, expense_type):
    """
    This function prints all the expenses of a given type

    :param expense_list:
    :param expense_type:
    :return:
    """
    validator_expense_type(expense_type)
    expense_list = expense_list_sort_day(expense_list)
    for expense in expense_list:
        if get_expense_type(expense) == expense_type:
            print(f"Day {get_day(expense)}  {get_amount(expense)}  {get_expense_type(expense)}")


def print_expenses_type_greater(expense_list, expense_type, value):
    """
    This function prints all the expenses of a given type that have a greater amount value than the value parameter

    :param expense_list:
    :param expense_type:
    :param value:
    :return:
    """
    validator_expense_type(expense_type)
    expense_list = expense_list_sort_day(expense_list)
    for expense in expense_list:
        if get_expense_type(expense) == expense_type and get_amount(expense) > value:
            print(f"Day {get_day(expense)}  {get_amount(expense)}  {get_expense_type(expense)}")


def print_expenses_type_lower(expense_list, expense_type, value):
    """
    This function prints all the expenses of a given type that have a lower amount value than the value parameter

    :param expense_list:
    :param expense_type:
    :param value:
    :return:
    """
    validator_expense_type(expense_type)
    expense_list = expense_list_sort_day(expense_list)
    for expense in expense_list:
        if get_expense_type(expense) == expense_type and get_amount(expense) < value:
            print(f"Day {get_day(expense)}  {get_amount(expense)}  {get_expense_type(expense)}")


def print_expenses_type_equal(expense_list, expense_type, value):
    """
    This function prints all the expenses of a given type that have an equal amount value with the value parameter

    :param expense_list:
    :param expense_type:
    :param value:
    :return:
    """
    validator_expense_type(expense_type)
    expense_list = expense_list_sort_day(expense_list)
    for expense in expense_list:
        if get_expense_type(expense) == expense_type and get_amount(expense) == value:
            print(f"Day {get_day(expense)}  {get_amount(expense)}  {get_expense_type(expense)}")


def print_sum_expenses_type(expense_list, expense_type):
    validator_expense_type(expense_type)

    sum_expenses = sum_expenses_type(expense_list, expense_type)
    print(f"The sum is {sum_expenses} \n")


def print_max_day_expenses(expense_list):

    max_day = max_day_expenses(expense_list)
    print(f"The day with the maximum amount of expenses is day {max_day} \n")


def print_sort_type(expense_list, expense_type):
    validator_expense_type(expense_type)
    expense_list = sort_type(expense_list, expense_type)
    for expense in expense_list:
        print(f"Day {get_day(expense)}  {get_amount(expense)}  {get_expense_type(expense)}")


def get_command_and_args(cmd_line):
    split_words = cmd_line.split(" ")
    words = []
    numbers = []
    operator = ''
    for character in split_words:
        if character.isnumeric():
            numbers.append(character)
        elif character.isalpha():
            words.append(character)
        elif character == '<':
            operator = '<'
        elif character == '=':
            operator = '='
        elif character == '>':
            operator = '>'

    return words, numbers, operator


def print_commands_start():
    print(f"Hello and welcome to the Family Expenses Manager\n"
          f"Please introduce one of the following commands: \n"
          f"1. add <sum> <category> \n"
          f"2. insert <day> <sum> <category> \n"
          f"3. remove \n"
          f"      > remove <day> \n"
          f"      > remove <start day> to <end day> \n"
          f"      > remove <category> \n"
          f"4. list \n"
          f"     > list \n"
          f"     > list <category> \n"
          f"     > list <category> [ < | = | > ] <value> \n"
          f"5. sum <category> \n"
          f"6. max day \n"
          f"7. sort  \n"
          f"     > sort day \n"
          f"     > sort <category> \n"
          f"8. filter \n"
          f"      > filter <category> \n"
          f"      > filter <category> [ < | = | > ] <value> \n"
          f"9. undo \n"
          f"10. exit \n")


def ui_add_expense(expense_list, amount, expense_type):
    validator_amount(amount)
    validator_expense_type(expense_type)

    add_expense(expense_list, int(amount), expense_type)
    print(f"The expense has been added ! \n")


def validator_day(day):
    if day.isnumeric():
        day = int(day)
        if 1 <= day <= 31:
            raise ValueError(f"The day must be between 1 and 31 \n ")
    else:
        raise ValueError(f"The day value must be int\n ")


def validator_amount(amount):
    if amount.isnumeric():
        amount = int(amount)
        if amount < 0:
            raise ValueError(f"The amount value must be positive!! \n ")
    else:
        raise ValueError(f"The amount value must be int \n ")


def validator_expense_type(expense_type):
    if expense_type not in ['housekeeping', 'food', 'transport', 'internet', 'clothing', 'others']:
        raise ValueError(f"The category must be one of the following: "
                         f"housekeeping, food, transport, clothing, internet, others \n ")


def ui_insert_expense(expense_list, day, amount, expense_type):
    validator_day(day)
    validator_expense_type(expense_type)
    validator_amount(amount)

    insert_expense(expense_list, int(day), int(amount), expense_type)
    print(f"The expense has been added ! \n ")


def ui_remove_expense_day(expense_list, day):
    validator_day(day)

    remove_expense_day(expense_list, day)
    print(f"The expense has been removed ! \n ")


def ui_remove_expense_interval(expense_list, day1, day2):
    validator_day(day1)
    validator_day(day2)

    remove_expense_interval(expense_list, day1, day2)
    print(f"The expenses have been removed ! \n ")


def ui_remove_expense_type(expense_list, expense_type):
    validator_expense_type(expense_type)

    remove_expense_type(expense_list, expense_type)
    print(f"The expenses have been removed ! \n ")


def print_sort_by_amount(expense_list):
    expense_list = sort_by_amount(expense_list)
    print_all_expenses(expense_list)

    print(f"The expense list has been sorted ! \n ")


def ui_filter_expense_type(expense_list, expense_type):
    validator_expense_type(expense_type)

    filter_expense_type(expense_list, expense_type)
    print(f"The expense list has been filtered ! \n ")


def ui_filter_expense_type_greater(expense_list, expense_type, value):
    validator_expense_type(expense_type)
    validator_amount(value)

    filter_expense_type_greater(expense_list, expense_type, value)
    print(f"The expense list has been filtered ! \n ")


def ui_filter_expense_type_lower(expense_list, expense_type, value):
    validator_expense_type(expense_type)
    validator_amount(value)

    filter_expense_type_lower(expense_list, expense_type, value)
    print(f"The expense list has been filtered ! \n ")


def ui_filter_expense_type_equal(expense_list, expense_type, value):
    validator_expense_type(expense_type)
    validator_amount(value)

    filter_expense_type_equal(expense_list, expense_type, value)
    print(f"The expense list has been filtered ! \n ")
