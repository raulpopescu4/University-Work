package model.expressions;

import exceptions.MyException;
import model.dataStructures.MyIHeap;
import model.dataStructures.MyiDictionary;
import model.types.Type;
import model.values.Value;

public class VariableExpression implements ProgramExpression{
    String id;

    public VariableExpression(String _id){
        id = _id;
    }


    public Value evaluate(MyiDictionary<String, Value> table, MyIHeap heap) throws MyException {
        return table.lookUp(id);
    }

    public ProgramExpression createDeepCopy() {
        return new VariableExpression(id);
    }

    public Type typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        return typesTable.lookUp(this.id);
    }

    @Override
    public String toString(){
        return id;
    }
}
