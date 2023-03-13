package model.statements;

import exceptions.MyException;
import model.dataStructures.MyiDictionary;
import model.programState.ProgramState;
import model.types.Type;
import model.values.Value;

public class VariableDeclarationStatement implements IStatement {

    String name;
    Type type;

    public ProgramState execute(ProgramState state) throws MyException {
        MyiDictionary<String, Value> symbolsTable = state.getSymbolsTable();
        if(symbolsTable.isDefined(name))
            throw new MyException("Variable " + name + " is already declared!");

        symbolsTable.addSymbol(name, type.getDefaultValue());
        state.setSymbolsTable(symbolsTable);
        return null;
    }

    public IStatement createDeepCopy() {
        return new VariableDeclarationStatement(name, type);
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        typesTable.addSymbol(name, type);
        return typesTable;
    }

    public VariableDeclarationStatement(String _name, Type _type){
        name = _name;
        type = _type;
    }

    @Override
    public String toString(){
        return name + " " + type.toString();
    }

}
