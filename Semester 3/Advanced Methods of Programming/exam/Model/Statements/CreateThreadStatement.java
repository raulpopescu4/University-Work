package Model.Statements;

import Model.Exceptions.MyException;
import Model.DataStructures.*;
import Model.ProgramState.ProgramState;
import Model.Types.Type;
import Model.Values.Value;

// done for LAB06
public class CreateThreadStatement implements iStatement{
    iStatement statement;

    public CreateThreadStatement(iStatement _statement) {
        this.statement = _statement;
    }

    public ProgramState execute(ProgramState state) throws MyException {
        MyiStack<iStatement> newStack = new MyStack<>();

        MyiStack<MyiDictionary<String, Value>> symbolsTableDeepCopy = state.getSymbolsTable().createDeepCopy();

        return new ProgramState(this.statement, newStack, symbolsTableDeepCopy, state.getOutputValues(), state.getFileTable(), state.getHeapTable(), state.getProceduresTable());
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        this.statement.typeCheck(typesTable.createDeepCopy());

        return typesTable;
    }

    public iStatement createDeepCopy() {
        return new CreateThreadStatement(this.statement.createDeepCopy());
    }

    @Override
    public String toString() {
        return "CreateThread(" + this.statement.toString() + ")";
    }
}