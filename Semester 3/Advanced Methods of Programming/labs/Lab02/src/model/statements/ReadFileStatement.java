package model.statements;

import exceptions.MyException;
import model.programState.ProgramState;
import model.dataStructures.MyiDictionary;
import model.expressions.ProgramExpression;
import model.types.IntType;
import model.types.StringType;
import model.types.Type;
import model.values.StringValue;
import model.values.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class ReadFileStatement implements IStatement{
    ProgramExpression expression;
    String variableName;

    public ReadFileStatement(ProgramExpression _expression, String _variableName){
        expression = _expression;
        variableName = _variableName;
    }

    public ProgramState execute(ProgramState state) throws MyException{
        if(state.getFileTable().isDefined(variableName))
            throw new MyException(variableName + " is not contained in the symbols table!");

        Value value = state.getSymbolsTable().lookUp(variableName);
        if(!value.getType().equals(new IntType()))
            throw new MyException("The expression must be a IntType!");

        value = expression.evaluate(state.getSymbolsTable(), state.getHeapTable());
        if(!value.getType().equals(new StringType()))
            throw new MyException("The expression must be a StringType!");

        StringValue stringValue = (StringValue) value;
        if(!state.getFileTable().isDefined(stringValue.getValue()))
            throw new MyException("The file table does not contain the value" + stringValue);

        BufferedReader bufferedReader;

        try{
            bufferedReader = state.getFileTable().lookUp(stringValue.getValue());
            String currentLine = bufferedReader.readLine();
            if( currentLine == null)
                currentLine = "0";

            MyiDictionary<String, Value> symbolsTable = state.getSymbolsTable();

        } catch (IOException exception){
            throw new MyException("Could not read from the file " + stringValue);
        }


        return null;
    }

    public IStatement createDeepCopy(){
        return new ReadFileStatement(expression.createDeepCopy(), variableName);
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        Type expressionType = this.expression.typeCheck(typesTable);
        if (!expressionType.equals(new StringType()))
            throw new MyException("ReadFileStatement: A string must be provided as expression parameter!");

        Type variableType = typesTable.lookUp(this.variableName);
        if (!(variableType.equals(new IntType())))
            throw new MyException("ReadFileStatement: An int must be provided as variable parameter!");

        return typesTable;
    }

    @Override
    public String toString(){
        return "ReadFileStatement(" + expression + ", " + variableName + ")";
    }
}
