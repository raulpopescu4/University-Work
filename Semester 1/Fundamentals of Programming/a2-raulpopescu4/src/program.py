import traceback

# Write the implementation for A2 in this file


# UI section


# =================== UI ===================


def run_menu_cmd():
    complex_numbers = initialize_complex_numbers()

    options = {
        "1": ui_add_complex_number,
        "2": print_all_complex_numbers,
        "3": ui_real_numbers_sequence,
        "4": ui_distinct_numbers_sequence,
    }

    while True:
        print_menu_options()

        opt = input("Introduce the corresponding number of the command: ")
        if opt == "5":
            break
        else:
            if opt in options:
                options[opt](complex_numbers)
            else:
                print("You need to insert a number between 1 and 5 !!")


def ui_add_complex_number(complex_numbers):
    real = input("The real part: ")
    imaginary = input("The imaginary part: ")
    try:
        add_complex_number(complex_numbers, int(real), int(imaginary))
        print("The number has been added.")
    except ValueError as ve:
        print("Real and imaginary values must be int: ", ve)


def print_menu_options():
    print("1: Add complex number\n"
          "2: Show the list of complex numbers\n"
          "3: The longest sequence that has only real numbers\n"
          "4: The longest sequence that has distinct numbers\n"
          "5: Exit")


def print_all_complex_numbers(complex_numbers):
     for complex_number in complex_numbers :
       print(beautiful_print(get_real(complex_number,get_imaginary(complex_number))
    #for i in range(0, len(complex_numbers)):
       # print(beautiful_print(get_real(complex_numbers[i]), get_imaginary(complex_numbers[i])))


def ui_real_numbers_sequence(complex_numbers):
    sequence_elements = real_numbers_sequence(complex_numbers)
    for i in range(0, len(sequence_elements)):
        print(beautiful_print(get_real(complex_numbers[sequence_elements[i]]),
                              get_imaginary(complex_numbers[sequence_elements[i]])))


def ui_distinct_numbers_sequence(complex_numbers):
    sequence_elements = distinct_numbers_sequence(complex_numbers)
    for i in range(0, len(sequence_elements)):
        print(beautiful_print(get_real(complex_numbers[sequence_elements[i]]),
                              get_imaginary(complex_numbers[sequence_elements[i]])))


# Function section


# ======================= FUNCTION =======================


def distinct_numbers_sequence(complex_numbers):
    '''

    This function returns the position of the elements of the longest distinct numbers sequence

    :param complex_numbers:
    :return:
    '''

    sequence_length = 0
    max_sequence_length = 0
    max_sequence_elements = []
    sequence_elements = []
    for i in range(0, len(complex_numbers)-1):
        if complex_numbers[i] != complex_numbers[i+1]:
            sequence_length += 1
            sequence_elements.append(i)
        elif sequence_length > max_sequence_length:
            max_sequence_length = sequence_length
            max_sequence_elements = sequence_elements
            sequence_length = 1
            sequence_elements = []
        else:
            sequence_length = 1
            sequence_elements = []

    if complex_numbers[i] != complex_numbers[i+1]:
            sequence_length += 1
            sequence_elements.append(i+1)

    if sequence_length > max_sequence_length:
        max_sequence_length = sequence_length
        max_sequence_elements = sequence_elements
        sequence_length = 1
        sequence_elements = []
    else:
        sequence_length = 1
        sequence_elements = []

    return max_sequence_elements


def real_numbers_sequence(complex_numbers):
    '''

    This function returns the position of the elements of the longest real numbers sequence

    :param complex_numbers:

    :return:
    '''

    sequence_length = 0
    max_sequence_length = 0
    max_sequence_elements = []
    sequence_elements = []
    for i in range(0, len(complex_numbers)):
        if get_imaginary(complex_numbers[i]) == 0:
            sequence_length += 1
            sequence_elements.append(i)
        elif sequence_length > max_sequence_length:
            max_sequence_length = sequence_length
            max_sequence_elements = sequence_elements
            sequence_length = 0
            sequence_elements = []
        else:
            sequence_length = 0
            sequence_elements = []

    if sequence_length > max_sequence_length:
        max_sequence_length = sequence_length
        max_sequence_elements = sequence_elements
        sequence_length = 0
        sequence_elements = []
    else:
        sequence_length = 0
        sequence_elements = []

    return max_sequence_elements


def beautiful_print(real, imaginary):
    '''

    This function creates a string representing a complex number that is used for printing

    :param real: The real part of the complex number
    :param imaginary: The imaginary part of the complex number
    :return:
    '''
    # imaginary = 0 or real = 0
    # imaginary = +-1
    # imaginary < 0
    # imaginary > 0
    # real != 0
    real_string = ""
    imaginary_string = ""
    if imaginary == 1:
        imaginary_string = "+i"
    elif imaginary == -1:
        imaginary_string = "-i"
    elif imaginary < 0:
        imaginary_string = f"{imaginary}i"
    elif imaginary > 0:
        imaginary_string = f"+{imaginary}i"
    if not real == 0:
        real_string = f"{real}"
    complex_number_string = real_string + imaginary_string
    return complex_number_string


def get_real(complex_number):
    return complex_number["real"]


def get_imaginary(complex_number):
    return complex_number["imaginary"]


def set_real(complex_number, real):
    complex_number["real"] = real


def set_imaginary(complex_number, imaginary):
    complex_number["imaginary"] = imaginary


def create_complex_number(real, imaginary):
    '''

    This function creates a complex number

    :param real: The real part
    :param imaginary: The imaginary part
    :return:
    '''

    complex_number = {
        "real": real,
        "imaginary": imaginary
    }
    return complex_number


def initialize_complex_numbers():
    '''

    This functions initialize a preset list of complex numbers

    :return:
    '''

    complex_numbers = []

    add_complex_number(complex_numbers, 4, 2)
    add_complex_number(complex_numbers, 3, 1)
    add_complex_number(complex_numbers, -2, 1)
    add_complex_number(complex_numbers, 0, -1)
    add_complex_number(complex_numbers, 10, 5)
    add_complex_number(complex_numbers, 7, -1)
    add_complex_number(complex_numbers, -2, -9)
    add_complex_number(complex_numbers, 3, -14)
    add_complex_number(complex_numbers, 12, 0)
    add_complex_number(complex_numbers, 5, 0)

    return complex_numbers


def add_complex_number(complex_numbers, real, imaginary):
    '''

    This function adds a new complex number to the list of complex numbers.

    :param complex_numbers:
    :param real:
    :param imaginary:
    :return:
    '''

    complex_number = create_complex_number(real, imaginary)
    complex_numbers.append(complex_number)


# ============================ TEST ==========================


def test_create_complex_number():
    complex_number = create_complex_number(3, 4)
    assert complex_number["real"] == 3
    assert complex_number["imaginary"] == 4


def test_add_complex_number():
    complex_numbers = initialize_complex_numbers()
    add_complex_number(complex_numbers, 3, 4)
    add_complex_number(complex_numbers, 6, 3)
    assert len(complex_numbers) == 12


def test_real_numbers_sequence():
    complex_numbers = initialize_complex_numbers()
    add_complex_number(complex_numbers, 5, 3)
    add_complex_number(complex_numbers, 3, 0)
    add_complex_number(complex_numbers, 2, 0)
    add_complex_number(complex_numbers, 3, 4)
    add_complex_number(complex_numbers, 8, 0)
    add_complex_number(complex_numbers, 7, 0)
    add_complex_number(complex_numbers, 6, 0)
    add_complex_number(complex_numbers, 1, 0)

    real_sequence = real_numbers_sequence(complex_numbers)
    assert len(real_sequence) == 4


def test_distinct_numbers_sequence():
    complex_numbers = []
    add_complex_number(complex_numbers, 5, 3)
    add_complex_number(complex_numbers, 3, 0)
    add_complex_number(complex_numbers, 2, 0)
    add_complex_number(complex_numbers, 3, 4)
    add_complex_number(complex_numbers, 3, 4)
    add_complex_number(complex_numbers, 7, 0)
    add_complex_number(complex_numbers, 6, 0)
    add_complex_number(complex_numbers, 1, 0)
    add_complex_number(complex_numbers, 2, 0)

    numbers_sequence = distinct_numbers_sequence(complex_numbers)
    assert len(numbers_sequence) == 5


def test_all():
    test_create_complex_number()
    test_add_complex_number()
    test_real_numbers_sequence()
    test_distinct_numbers_sequence()


# ==================== MAIN ============================


if __name__ == '__main__':

    test_all()

    try:
        run_menu_cmd()
    except Exception as ex:
        print("Unknown exception caught: ", ex)
        traceback.print_exc()
