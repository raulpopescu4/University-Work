import traceback
from UI import *
from Tests import test_all
from Functions import *


if __name__ == '__main__':

    test_all()

    try:
        run_menu_cmd()
    except Exception as ex:
        print("Unknown exception caught: ", ex)
        traceback.print_exc()
