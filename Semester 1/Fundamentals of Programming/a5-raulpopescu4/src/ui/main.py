from src.ui.UI import ExpenseUI
from src.services.UnitTest import UnitTest


def test_all():
    test = UnitTest()
    test.test_all()


def main():
    start_program = ExpenseUI()
    start_program.start_menu()


if __name__ == '__main__':
    test_all()
    main()
