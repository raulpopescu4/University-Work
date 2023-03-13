package model.expressions;

import exceptions.MyException;
import model.dataStructures.MyIHeap;
import model.dataStructures.MyiDictionary;
import model.types.Type;
import model.values.Value;

public class ValueExpression implements ProgramExpression{
    Value expression;

    public ValueExpression(Value _expression){
        expression =_expression;
    }

    public Value evaluate(MyiDictionary<String, Value> table, MyIHeap heap) throws MyException{
        return expression;
    }

    public ProgramExpression createDeepCopy() {
        return new ValueExpression(expression);
    }

    public Type typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        return expression.getType();
    }

    @Override
    public String toString(){
        return expression.toString();
    }
}
