package model.statements;

import exceptions.MyException;
import model.dataStructures.MyiDictionary;
import model.dataStructures.MyiStack;
import model.programState.ProgramState;
import model.types.Type;

public class CompoundStatement implements IStatement {
    IStatement first;
    IStatement second;

    public CompoundStatement(IStatement _first, IStatement _second){
        first = _first;
        second = _second;
    }

    public ProgramState execute(ProgramState state) throws MyException{
        MyiStack<IStatement> statementStack = state.getExecutionStack();
        statementStack.push(second);
        statementStack.push(first);
        return null;
    }

    public IStatement createDeepCopy() {
        return new CompoundStatement(first.createDeepCopy(), second.createDeepCopy());
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        return second.typeCheck(first.typeCheck(typesTable));
    }

    @Override
    public String toString(){
        return "(" + first.toString() + ";" + second.toString() + ")";
    }




}
