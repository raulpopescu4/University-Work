from symbolTable import SymbolTable


def test_hash_table(symbol_table):

    print(f"{symbol_table.exists('1')}")
    print(f"{symbol_table.exists('2')}")
    print(f"{symbol_table.exists('4')}")

    position_first = symbol_table.search('1')
    position_second = symbol_table.search('2')

    print(f"Position of '1': {position_first}")
    print(f"Position of '2': {position_second}")

    position1 = symbol_table.add('1')
    position2 = symbol_table.add('1')

    print(f"Position of the first '1': {position1}")
    print(f"Position of the second '1': {position2}")

    print(symbol_table)

    try:
        symbol_table.remove('1')
        # This will throw ValueError
        symbol_table.remove('4')
    except ValueError as e:
        print(f"Caught ValueError: {e}")


if __name__ == "__main__":
    symbol_table = SymbolTable(5)

    # Add symbols to the SymbolTable
    symbol_table.add('1')
    symbol_table.add('2')
    symbol_table.add('3')

    # Run tests on the HashTable through the SymbolTable
    test_hash_table(symbol_table)

    print(symbol_table)
