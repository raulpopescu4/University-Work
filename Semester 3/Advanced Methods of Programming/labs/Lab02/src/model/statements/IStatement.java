package model.statements;

import exceptions.MyException;
import model.dataStructures.MyiDictionary;
import model.programState.ProgramState;
import model.types.Type;

public interface IStatement {
    ProgramState execute(ProgramState state) throws MyException;

    public IStatement createDeepCopy();

    MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException;
}