package model.statements;

import exceptions.MyException;
import model.programState.ProgramState;
import model.dataStructures.MyiDictionary;
import model.expressions.ProgramExpression;
import model.types.StringType;
import model.types.Type;
import model.values.StringValue;
import model.values.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class CloseReadFileStatement implements IStatement{

    ProgramExpression expression;

    public CloseReadFileStatement(ProgramExpression _expression){
        expression = _expression;
    }

    public ProgramState execute(ProgramState state) throws MyException {
        Value value = expression.evaluate(state.getSymbolsTable(), state.getHeapTable());
        if (!value.getType().equals(new StringType()))
            throw new MyException("The expression must be a StringType!");

        StringValue stringValue = (StringValue) value;
        if (!state.getFileTable().isDefined(stringValue.getValue()))
            throw new MyException("The file was not found!");

        BufferedReader bufferedReader;

        try{
            bufferedReader = state.getFileTable().lookUp(stringValue.getValue());
            bufferedReader.close();
        } catch (IOException exception){
            throw new MyException(stringValue + " file could not be closed!");
        }

        MyiDictionary<String, BufferedReader> fileTable = state.getFileTable();
        fileTable.removeSymbol(stringValue.getValue());
        state.setFileTable(fileTable);


        return null;
    }

    public IStatement createDeepCopy() {
        return new CloseReadFileStatement(expression.createDeepCopy());
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        if (!(this.expression.typeCheck(typesTable).equals(new StringType())))
            throw new MyException("Close ReadFile Statement: A string expression must be provided!");

        return typesTable;
    }

    @Override
    public String toString(){
        return "CloseReadFileStatement(" + expression + ")";
    }
}
