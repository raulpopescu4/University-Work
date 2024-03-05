import datetime
import copy

def initialize_expenses():
    """"
    Initializes a predefined list of expenses

    :return:
    """
    expense_list = []
    insert_expense(expense_list, 1, 40, 'transport')
    insert_expense(expense_list, 1, 50, 'internet')
    insert_expense(expense_list, 2, 200, 'others')
    insert_expense(expense_list, 3, 500, 'housekeeping')
    insert_expense(expense_list, 4, 120, 'food')
    insert_expense(expense_list, 5, 200, 'clothing')
    insert_expense(expense_list, 5, 40, 'others')
    insert_expense(expense_list, 7, 35, 'transport')
    insert_expense(expense_list, 8, 100, 'food')
    insert_expense(expense_list, 9, 60, 'others')
    insert_expense(expense_list, 10, 420, 'housekeeping')
    insert_expense(expense_list, 10, 20, 'transport')
    insert_expense(expense_list, 12, 150, 'food')
    insert_expense(expense_list, 15, 100, 'others')

    return expense_list


def create_expense(amount, expense_type):
    """
    This function creates an expense

    :param amount: The amount of money that have been spent(positive integer)
    :param expense_type: The type of expense(one of: housekeeping, food, transport, clothing, internet, others)
    :return:
    """

    expense = {
        "day": datetime.date.today().day,
        "amount": amount,
        "expense_type": expense_type
    }
    return expense


def get_day(expense):
    return expense["day"]


def get_amount(expense):
    return expense["amount"]


def get_expense_type(expense):
    return expense["expense_type"]


def set_day(expense, day):
    expense["day"] = day


def set_amount(expense, amount):
    expense["amount"] = amount


def set_expense_type(expense, expense_type):
    expense["expense_type"] = expense_type


def add_expense(expense_list, amount, expense_type):
    """
    This function adds a new expense to the list of expenses

    :param expense_list:
    :param amount:
    :param expense_type:
    :return:
    """

    expense = create_expense(amount, expense_type)
    expense_list.append(expense)


def insert_expense(expense_list, day, amount, expense_type):
    """
    This functions inserts a new expense in the list

    :param expense_list
    :param day:
    :param amount:
    :param expense_type:
    :return:
    """

    expense = create_expense(amount, expense_type)
    set_day(expense, day)
    expense_list.append(expense)


def remove_expense_day(expense_list, day):
    """"
    This function deletes all the expenses from a certain date

    :param expense_list:
    :param day:
    :return:
    """
    i = 0
    while i < len(expense_list):
        if get_day(expense_list[i]) == day:
            expense_list.pop(i)
        else:
            i += 1


def remove_expense_interval(expense_list, day1, day2):
    """
    This functions deletes all the expenses between a certain day interval

    :param expense_list:
    :param day1:
    :param day2:
    :return:
    """

    i = 0
    while i < len(expense_list):
        if day1 <= get_day(expense_list[i]) <= day2:
            expense_list.pop(i)
        else:
            i += 1


def remove_expense_type(expense_list, expense_type):
    """
    This function deletes all the expenses of a given type

    :param expense_list:
    :param expense_type:
    :return:
    """
    i = 0
    while i < len(expense_list):
        if get_expense_type(expense_list[i]) == expense_type:
            expense_list.pop(i)
        else:
            i += 1


def sum_expenses_type(expense_list, expense_type):
    """
    This function makes the sum of all the expenses of a given type

    :param expense_list:
    :param expense_type:
    :return:
    """

    expenses_sum = 0
    for expense in expense_list:
        if get_expense_type(expense) == expense_type:
            expenses_sum += get_amount(expense)

    return expenses_sum


def expense_list_sort_day(expense_list):
    """
    This function sorts the expenses from the expense list by day

    :param expense_list:
    :return:
    """

    for i in range(1, len(expense_list)):
        current_value = expense_list[i]
        pos = i

        while pos > 0 and get_day(expense_list[pos-1]) > get_day(current_value):
            expense_list[pos] = expense_list[pos-1]
            pos -= 1

        expense_list[pos] = current_value

    return expense_list


def max_day_expenses(expense_list):
    """
    This function returns the day with the maximum amount of expenses

    :param expense_list:
    :return:
    """
    max_expense_amount = 0
    for i in range(1, 31):
        if day_total(expense_list, i) > max_expense_amount:
            max_expense_amount = day_total(expense_list, i)
            max_day = i

    return max_day


def filter_expense_type(expense_list, expense_type):
    """
    This function filters the expense list by a given type of expense

    :param expense_list:
    :param expense_type:
    :return:
    """
    i = 0
    while i < len(expense_list):
        if get_expense_type(expense_list[i]) != expense_type:
            expense_list.pop(i)
        else:
            i += 1


def filter_expense_type_greater(expense_list, expense_type, value):
    """
    This function filters the expense list by a given type of expense and by having a greater amount value than the
    value given

    :param expense_list:
    :param expense_type:
    :param value:
    :return:
    """
    i = 0
    while i < len(expense_list):
        if get_expense_type(expense_list[i]) != expense_type or get_amount(expense_list[i]) <= value:
            expense_list.pop(i)
        else:
            i += 1


def filter_expense_type_lower(expense_list, expense_type, value):
    """
    This function filters the expense list by a given type of expense and by having a lower amount value than the
    value given

    :param expense_list:
    :param expense_type:
    :param value:
    :return:
    """
    i = 0
    while i < len(expense_list):
        if get_expense_type(expense_list[i]) != expense_type or get_amount(expense_list[i]) >= value:
            expense_list.pop(i)
        else:
            i += 1


def filter_expense_type_equal(expense_list, expense_type, value):
    """
    This function filters the expense list by a given type of expense and by having an equal amount value with the
    value given

    :param expense_list:
    :param expense_type:
    :param value:
    :return:
    """
    i = 0
    while i < len(expense_list):
        if get_expense_type(expense_list[i]) != expense_type or get_amount(expense_list[i]) != value:
            expense_list.pop(i)
        else:
            i += 1


def day_total(expense_list, day):
    """
    This function calculates and returns the amount of money spent in a given day

    :param expense_list:
    :param day:
    :return:
    """
    day_amount = 0
    for expense in expense_list:
        if get_day(expense) == day:
            day_amount += get_amount(expense)

    return day_amount


def sort_type(expense_list, expense_type):
    """
    This function sorts the expenses that have the given type in an ascending order

    :param expense_list:
    :param expense_type:
    :return:
    """
    filter_expense_type(expense_list, expense_type)
    for i in range(1, len(expense_list)):
        current_value = expense_list[i]
        pos = i

        while pos > 0 and get_amount(expense_list[pos-1]) > get_amount(current_value):
            expense_list[pos] = expense_list[pos-1]
            pos -= 1

        expense_list[pos] = current_value

    return expense_list


def sort_by_amount(expense_list):
    """
    This function sorts the expense list by amount in an ascending order

    :param expense_list:
    :return:
    """
    for i in range(1, len(expense_list)):
        current_value = expense_list[i]
        pos = i

        while pos > 0 and get_amount(expense_list[pos-1]) > get_amount(current_value):
            expense_list[pos] = expense_list[pos-1]
            pos -= 1

        expense_list[pos] = current_value

    return expense_list


def add_last_operation_performed(expense_list_history, expense_list):
    expense_list_history.append(copy.deepcopy(expense_list))


def undo(expense_list_history):
    if len(expense_list_history) > 0:
        last_expense_list = copy.deepcopy(expense_list_history[-1])
        expense_list_history.pop(-1)
        return last_expense_list
    else:
        raise ValueError("There is no operation to be undone")














