package Model.Statements;

import Model.Exceptions.MyException;
import Model.DataStructures.MyiDictionary;
import Model.DataStructures.MyiStack;
import Model.ProgramState.ProgramState;
import Model.Types.Type;
import Model.Values.Value;

// done for LAB06
public class VariableDeclarationStatement implements iStatement {
    String name;
    Type type;

    public VariableDeclarationStatement(String _name, Type _type) {
        this.name = _name;
        this.type = _type;
    }

    public ProgramState execute(ProgramState state) throws MyException {
        MyiStack<MyiDictionary<String, Value>> symbolsTable = state.getSymbolsTable();
        MyiDictionary<String, Value> currentSymbolTable = symbolsTable.peek();

        if (currentSymbolTable.isDefined(this.name))
            throw new MyException("Variable " + this.name + " is already declared!");

        currentSymbolTable.add(this.name, this.type.getDefaultValue());
        state.setSymbolsTable(symbolsTable);

        return null;
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        typesTable.add(this.name, this.type);
        return typesTable;
    }

    public iStatement createDeepCopy() {
        return new VariableDeclarationStatement(this.name, this.type);
    }

    @Override
    public String toString() {
        return this.type.toString() + " " + this.name;
    }
}
