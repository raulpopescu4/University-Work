package model.statements;

import exceptions.MyException;
import model.dataStructures.MyiDictionary;
import model.programState.ProgramState;
import model.types.Type;

public class NoOperationStatement implements IStatement {

    public ProgramState execute(ProgramState state) throws MyException {
        return null;
    }

    public IStatement createDeepCopy() {
        return new NoOperationStatement();
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        return typesTable;
    }

    @Override
    public String toString(){
        return "NoOperation Statement";
    }
}
