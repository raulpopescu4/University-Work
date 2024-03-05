class UndoServiceException(Exception):
    pass


class UndoRedoServices:
    def __init__(self):
        # History of program operations, is a stack
        self._history = []
        self._index = -1

    def undo(self):
        if self._index < 0:
            raise UndoServiceException("No more undo!")
        else:
            self._history[self._index].undo()
            self._index -= 1

    def redo(self):
        if self._index + 1 >= len(self._history):
            raise UndoServiceException("No more redo!")
        else:
            self._index += 1
            self._history[self._index].redo()

    def record(self, operation):
        self._history.append(operation)
        self._index += 1


class Operation:
    """
    In this class it's stored each performed operation's inverse and reverse operation with the parameters
    """
    def __init__(self, undo_call, redo_call):
        self._undo_call = undo_call
        self._redo_call = redo_call

    def undo(self):
        self._undo_call.call()

    def redo(self):
        self._redo_call.call()


class ComplexOperation:
    def __init__(self, operation):
        self._operations = operation

    def undo(self):
        for operation in self._operations:
            operation.undo()

    def redo(self):
        for operation in self._operations:
            operation.redo()


class Call:
    def __init__(self, function_name, *function_params):
        self._function_name = function_name
        self._function_params = function_params

    def call(self):
        """
        The function is being called with its parameters
        :return:
        """
        self._function_name(*self._function_params)
