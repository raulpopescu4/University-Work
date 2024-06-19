
def get_day(expense):
    return expense["ziua"]


def remove_expense_day(expense_list, day):
    i = 0
    while i < len(expense_list):
        if get_day(expense_list[i]) == day:
            expense_list.pop(day)
        i += 1



        while True:
            print_commands_start()
            cmd_line = input()
            words, numbers, operator = get_command_and_args(cmd_line)
            for word in words:
                if word not in ['add', 'insert', 'remove', 'to', 'list', 'sum', 'max', 'day', 'sort', 'filter', 'undo',
                                'housekeeping', 'food', 'transport', 'internet', 'clothing', 'others']:
                    print(f"{word} is an invalid command, please try to introduce one of the given commands.")
                    raise KeyError
            if 'add' in words:
                pass
            elif 'insert' in words:
                pass
            elif words == ['remove']:
                pass
            elif words == ['remove', 'to']:
                pass
            elif words == ['list']:
                pass
            elif 'list' in words and len(numbers) == 1 and len(words) == 2 and operator:
                pass


['housekeeping', 'food', 'transport', 'internet', 'clothing', 'others']




            if words[0] not in ['add', 'insert', 'remove', 'sum', 'max', 'sort', 'filter', 'undo']:
                print(f"The inserted command is invalid. Please insert one of the given commands !\n")
            elif words[0] == 'add':
                cmd_line = input(f"Please insert the command as shown(category :")
                words, numbers, operator = get_command_and_args(cmd_line)
                ui_