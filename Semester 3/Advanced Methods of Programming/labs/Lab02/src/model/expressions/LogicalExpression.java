package model.expressions;

import exceptions.MyException;
import model.dataStructures.MyIHeap;
import model.dataStructures.MyiDictionary;
import model.types.BoolType;
import model.types.Type;
import model.values.BoolValue;
import model.values.Value;

import java.util.Objects;

public class LogicalExpression implements ProgramExpression{
    ProgramExpression e1;
    ProgramExpression e2;
    String operation;

    public LogicalExpression(ProgramExpression _e1, ProgramExpression _e2, String _operation){
        e1 = _e1;
        e2 = _e2;
        operation = _operation;
    }

    public Value evaluate(MyiDictionary<String, Value> table, MyIHeap heap) throws MyException {
        if(!Objects.equals(operation, "and") && !Objects.equals(operation,"or"))
            throw new MyException(operation + " is not a valid operation! ");

        Value v1 = e1.evaluate(table, heap);
        if(v1.getType().equals(new BoolType()))
            throw new MyException(e1 + " is not a boolean! ");

        Value v2 = e2.evaluate(table, heap);
        if(v2.getType().equals(new BoolType()))
            throw new MyException(e2 + " is not a boolean! ");

        BoolValue b1 = (BoolValue) e1;
        BoolValue b2 = (BoolValue) e2;

        if(Objects.equals(operation, "and"))
            return new BoolValue(b1.getValue() && b2.getValue());

        if (Objects.equals(operation, "or"))
            return new BoolValue(b1.getValue() || b2.getValue());

        return null;
    }

    public ProgramExpression createDeepCopy() {
        return new LogicalExpression(e1, e2, operation);
    }

    public Type typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        Type firstExpressionType = this.e1.typeCheck(typesTable);
        Type secondExpressionType = this.e2.typeCheck(typesTable);

        if (!firstExpressionType.equals(new BoolType()))
            throw new MyException("LogicalExpression: First operand is not a boolean expression!");

        if (!secondExpressionType.equals(new BoolType()))
            throw new MyException("LogicalExpression: Second operand is not a boolean expression!");

        return new BoolType();
    }

    @Override
    public String toString(){
        return e1.toString() + " " + operation + " " + e2.toString();
    }
}
