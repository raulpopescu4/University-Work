package model.statements;

import exceptions.MyException;
import model.dataStructures.MyDictionary;
import model.dataStructures.MyStack;
import model.dataStructures.MyiDictionary;
import model.dataStructures.MyiStack;
import model.programState.ProgramState;
import model.types.Type;
import model.values.Value;

import java.util.Map;

public class CreateThreadStatement implements IStatement{

    IStatement statement;

    public CreateThreadStatement(IStatement statement){
        this.statement = statement;
    }

    public ProgramState execute(ProgramState state) throws MyException {
        MyiStack<IStatement> newStack = new MyStack<>();

        MyiDictionary<String, Value> symbolsTable = state.getSymbolsTable();
        MyiDictionary<String, Value> symbolsTableDeepCopy = new MyDictionary<>();

        for (Map.Entry<String, Value> entry: symbolsTable.getContent().entrySet())
            symbolsTableDeepCopy.addSymbol(entry.getKey(), entry.getValue().createDeepCopy());

        return new ProgramState(this.statement, newStack, symbolsTableDeepCopy, state.getOutputValues(), state.getFileTable(), state.getHeapTable());
    }

    public IStatement createDeepCopy() {
        return new CreateThreadStatement(this.statement.createDeepCopy());
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        this.statement.typeCheck(typesTable.createDeepCopy());

        return typesTable;
    }

    @Override
    public String toString(){
        return "CreateThread(" + this.statement.toString() + ")";
    }
}
