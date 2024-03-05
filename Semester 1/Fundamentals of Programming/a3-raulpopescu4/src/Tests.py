from Functions import *


def test_all():
    test_create_expense()
    test_add_expense()
    test_insert_expense()
    test_remove_expense_day()
    test_remove_expense_interval()
    test_remove_expense_type()
    test_sum_expenses_type()
    test_max_day_expenses()
    test_filter_expense_type()
    test_filter_expense_type_greater()
    test_filter_expense_type_lower()
    test_filter_expense_type_equal()
    test_day_total()
    test_sort_type()
    test_sort_by_amount()
    test_undo()


def test_create_expense():
    expense = create_expense(4, 7)
    assert (expense["amount"] == 4)
    assert (expense["expense_type"] == 7)


def test_add_expense():
    expense_list = []
    add_expense(expense_list, 5, 3)
    add_expense(expense_list, 1, 8)
    add_expense(expense_list, 5, 3)
    add_expense(expense_list, 5, 3)
    add_expense(expense_list, 5, 3)

    assert(len(expense_list) == 5)


def test_insert_expense():
    expense_list = []
    insert_expense(expense_list, 3, 2, 1)
    insert_expense(expense_list, 3, 2, 1)
    insert_expense(expense_list, 3, 2, 1)
    insert_expense(expense_list, 3, 2, 1)
    insert_expense(expense_list, 3, 2, 1)

    assert (len(expense_list) == 5)
    assert (expense_list[0]["day"] == 3)


def test_remove_expense_day():
    expense_list = initialize_expenses()
    remove_expense_day(expense_list, 1)
    assert (len(expense_list) == 12)


def test_remove_expense_interval():
    expense_list = initialize_expenses()
    insert_expense(expense_list, 4, 2, 1)
    insert_expense(expense_list, 4, 2, 1)
    insert_expense(expense_list, 4, 2, 1)
    insert_expense(expense_list, 4, 2, 1)
    remove_expense_interval(expense_list, 1, 3)
    assert (len(expense_list) == 14)

    expense_list = initialize_expenses()
    insert_expense(expense_list, 4, 2, 1)
    insert_expense(expense_list, 4, 2, 1)
    insert_expense(expense_list, 4, 2, 1)
    insert_expense(expense_list, 4, 2, 1)
    remove_expense_interval(expense_list, 3, 10)
    assert (len(expense_list) == 5)


def test_remove_expense_type():
    expense_list = initialize_expenses()
    remove_expense_type(expense_list, 'transport')
    assert (len(expense_list) == 11)

    expense_list = initialize_expenses()
    remove_expense_type(expense_list, 'fasdwafwa')
    assert (len(expense_list) == 14)


def test_sum_expenses_type():
    expense_list = initialize_expenses()
    expense_sum = sum_expenses_type(expense_list, 'transport')
    assert (expense_sum == 95)


def test_max_day_expenses():
    expense_list = initialize_expenses()
    day = max_day_expenses(expense_list)
    assert(day == 3)


def test_filter_expense_type():
    expense_list = initialize_expenses()
    filter_expense_type(expense_list, 'others')
    assert (len(expense_list) == 4)


def test_filter_expense_type_greater():
    expense_list = initialize_expenses()
    filter_expense_type_greater(expense_list, 'food', 100)
    assert (len(expense_list) == 2)


def test_filter_expense_type_lower():
    expense_list = initialize_expenses()
    filter_expense_type_lower(expense_list, 'others', 200)
    assert (len(expense_list) == 3)


def test_filter_expense_type_equal():
    expense_list = initialize_expenses()
    filter_expense_type_equal(expense_list, 'others', 60)
    assert (len(expense_list) == 1)


def test_day_total():
    expense_list = initialize_expenses()
    day = 5
    assert(day_total(expense_list, day) == 240)


def test_sort_type():
    expense_list = initialize_expenses()
    expense_list = sort_type(expense_list, 'food')
    comparison_expense_list = []
    insert_expense(comparison_expense_list, 8, 100, 'food')
    insert_expense(comparison_expense_list, 4, 120, 'food')
    insert_expense(comparison_expense_list, 12, 150, 'food')
    assert(expense_list == comparison_expense_list)


def test_sort_by_amount():
    expense_list = []
    insert_expense(expense_list, 8, 100, 'food')
    insert_expense(expense_list, 12, 150, 'food')
    insert_expense(expense_list, 4, 120, 'food')
    expense_list = sort_by_amount(expense_list)
    comparison_expense_list = []
    insert_expense(comparison_expense_list, 8, 100, 'food')
    insert_expense(comparison_expense_list, 4, 120, 'food')
    insert_expense(comparison_expense_list, 12, 150, 'food')

    assert(expense_list == comparison_expense_list)


def test_undo():
    expense_list_history = list()
    expense_list = initialize_expenses()
    add_last_operation_performed(expense_list_history, expense_list)
    filter_expense_type(expense_list, 'others')
    expense_list = undo(expense_list_history)
    assert(len(expense_list) == 14)

