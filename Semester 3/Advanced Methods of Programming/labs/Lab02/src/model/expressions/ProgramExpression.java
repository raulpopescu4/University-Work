package model.expressions;

import exceptions.MyException;
import model.dataStructures.MyIHeap;
import model.dataStructures.MyiDictionary;
import model.types.Type;
import model.values.Value;

public interface ProgramExpression {
    Value evaluate(MyiDictionary<String, Value> table, MyIHeap heap) throws MyException;

    ProgramExpression createDeepCopy();

    Type typeCheck(MyiDictionary<String, Type> typesTable) throws MyException;
}
