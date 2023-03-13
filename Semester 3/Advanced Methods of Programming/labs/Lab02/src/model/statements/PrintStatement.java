package model.statements;

import exceptions.MyException;
import model.dataStructures.MyiDictionary;
import model.dataStructures.MyiList;
import model.expressions.ProgramExpression;
import model.programState.ProgramState;
import model.types.Type;
import model.values.Value;

public class PrintStatement implements IStatement {
    ProgramExpression expression;

    public PrintStatement(ProgramExpression _expression){
        expression = _expression;
    }

    public ProgramState execute(ProgramState state) throws MyException {
        MyiList<Value> outputValues = state.getOutputValues();

        outputValues.add(expression.evaluate(state.getSymbolsTable(), state.getHeapTable()));

        state.setOutputValues(outputValues);

        return null;
    }

    public IStatement createDeepCopy() {
        return new PrintStatement(expression.createDeepCopy());
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        expression.typeCheck(typesTable);
        return typesTable;
    }

    @Override
    public String toString(){
        return "print(" + expression.toString() + ")";
    }


}
