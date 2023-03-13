package model.statements;

import exceptions.MyException;
import model.programState.ProgramState;
import model.dataStructures.MyIHeap;
import model.dataStructures.MyiDictionary;
import model.expressions.ProgramExpression;
import model.types.ReferenceType;
import model.types.Type;
import model.values.ReferenceValue;
import model.values.Value;

public class HeapWritingStatement implements IStatement{

    String variableName;
    ProgramExpression expression;

    public HeapWritingStatement(String variableName, ProgramExpression expression){
        this.variableName = variableName;
        this.expression = expression;
    }

    public ProgramState execute(ProgramState state) throws MyException {
        MyiDictionary<String, Value> symbolsTable = state.getSymbolsTable();

        if(!symbolsTable.isDefined(variableName))
            throw new MyException("Variable " + variableName + "is not defined in the symbols table!");

        Value value = symbolsTable.lookUp(variableName);

        if(!(value.getType() instanceof ReferenceType))
            throw new MyException(variableName + "'s value type must be of type ReferenceType!");

        MyIHeap heap = state.getHeapTable();

        Value expressionValue = expression.evaluate(symbolsTable, heap);
        Type locationType = ((ReferenceValue)value).getLocationType();

        if(!expressionValue.getType().equals(locationType))
            throw new MyException("The variable and the expression must be of the same type!");

        heap.updateSymbol(((ReferenceValue)value).getAddress(), expressionValue);

        state.setHeapTable(heap);

        return null;
    }

    public IStatement createDeepCopy() {
        return new HeapWritingStatement(variableName, expression.createDeepCopy());
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        Type variableType = typesTable.lookUp(this.variableName);
        Type expressionType = this.expression.typeCheck(typesTable);

        if (!(variableType.equals(new ReferenceType(expressionType))))
            throw new MyException("Heap Writing Statement: Right hand side and left hand side have different types!");

        return typesTable;
    }

    @Override
    public String toString(){
        return "HeapWritingStatement(" + variableName + ", " + expression.toString() + ")";
    }

}
