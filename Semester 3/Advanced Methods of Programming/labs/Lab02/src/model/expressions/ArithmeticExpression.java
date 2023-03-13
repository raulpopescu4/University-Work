package model.expressions;


import exceptions.MyException;
import model.dataStructures.MyIHeap;
import model.dataStructures.MyiDictionary;
import model.types.IntType;
import model.types.Type;
import model.values.IntValue;
import model.values.Value;

public class ArithmeticExpression implements ProgramExpression{
    ProgramExpression e1;
    ProgramExpression e2;
    char operation; //1-plus, 2-minus, 3-star, 4-divide

    public ArithmeticExpression(char _operation, ProgramExpression _e1, ProgramExpression _e2){
        e1 = _e1;
        e2 = _e2;
        operation = _operation;
    }

    public Value evaluate(MyiDictionary<String, Value> table, MyIHeap heap) throws MyException{
        Value v1, v2;
        v1 = e1.evaluate(table, heap);

        if(v1.getType().equals(new IntType())){
            v2 = e2.evaluate(table, heap);
                    if(v2.getType().equals(new IntType())){
                        IntValue i1 = (IntValue) v1;
                        IntValue i2 = (IntValue) v2;
                        int n1, n2;
                        n1 = i1.getValue();
                        n2 = i2.getValue();

                        if(operation == '+') return new IntValue(n1 + n2);
                        if(operation == '-') return new IntValue(n1 - n2);
                        if(operation == '*') return new IntValue(n1 * n2);
                        if(operation == '/')
                            if(n2 == 0) throw new MyException("division by zero");
                                else return new IntValue(n1/n2);

                    }
                    else
                        throw new MyException("second operand is not an integer");
        }
        else throw new MyException("first operand is not an integer");

        return null;

    }

    public ProgramExpression createDeepCopy() {
        return new ArithmeticExpression(operation, e1, e2);
    }

    public Type typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        Type type1, type2;
        type1 = e1.typeCheck(typesTable);
        type2 = e2.typeCheck(typesTable);

        if(type1.equals(new IntType())){
            if(type2.equals(new IntType())){
                return new IntType();
            }else
                throw new MyException("The second operand is an not integer!");
        }else
            throw new MyException("The first operand is not an integer!");
    }

    @Override
    public String toString(){
        return e1.toString() + " " + operation + " " + e2.toString();
    }
}
