package model.expressions;

import exceptions.MyException;
import model.dataStructures.MyIHeap;
import model.dataStructures.MyiDictionary;
import model.types.BoolType;
import model.types.IntType;
import model.types.Type;
import model.values.BoolValue;
import model.values.IntValue;
import model.values.Value;

public class RelationalExpression implements ProgramExpression{
    ProgramExpression firstExpression;
    ProgramExpression secondExpression;
    String relation;

    public RelationalExpression(String _relation, ProgramExpression _firstExpression, ProgramExpression _secondExpression){
        firstExpression = _firstExpression;
        secondExpression = _secondExpression;
        relation = _relation;
    }


    public Value evaluate(MyiDictionary<String, Value> table, MyIHeap heap) throws MyException {
        Value firstValue, secondValue;
        firstValue = firstExpression.evaluate(table, heap);

        if(firstValue.getType().equals(new IntType())){
            secondValue = secondExpression.evaluate(table, heap);

            if(secondValue.getType().equals(new IntType())){
                IntValue firstInteger = (IntValue) firstValue;
                IntValue secondInteger = (IntValue) secondValue;

                int firstNumber, secondNumber;

                firstNumber = firstInteger.getValue();
                secondNumber = secondInteger.getValue();

                return switch (relation){
                    case "<" -> new BoolValue(firstNumber < secondNumber);

                    case "<=" -> new BoolValue(firstNumber <= secondNumber);

                    case "==" -> new BoolValue(firstNumber == secondNumber);

                    case "!=" -> new BoolValue(firstNumber != secondNumber);

                    case ">" -> new BoolValue(firstNumber > secondNumber);

                    case ">=" -> new BoolValue(firstNumber >= secondNumber);

                    default -> throw new MyException("Not a valid relation provided!");
                };
            } else
                throw new MyException("Second operand is not an integer!");
        } else
            throw new MyException("First operand is not an integer!");
    }

    public ProgramExpression createDeepCopy() {
        return new RelationalExpression(relation, firstExpression.createDeepCopy(), secondExpression.createDeepCopy());
    }

    public Type typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        Type firstExpressionType = this.firstExpression.typeCheck(typesTable);
        Type secondExpressionType = this.secondExpression.typeCheck(typesTable);

        if (!firstExpressionType.equals(new IntType()))
            throw new MyException("RelationalExpression: First operand is not an integer!");

        if (!secondExpressionType.equals(new IntType()))
            throw new MyException("RelationalExpression: Second operand is not an integer!");

        return new BoolType();
    }

    @Override
    public  String toString(){
        return firstExpression.toString() + " " + relation + " " + secondExpression.toString();
    }
}
