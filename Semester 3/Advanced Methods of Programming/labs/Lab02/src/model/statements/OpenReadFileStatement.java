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
import java.io.FileNotFoundException;
import java.io.FileReader;

public class OpenReadFileStatement implements IStatement{

    ProgramExpression expression;

    public OpenReadFileStatement(ProgramExpression _expression){
        expression =_expression;
    }

    public ProgramState execute(ProgramState state) throws MyException {
        Value value = expression.evaluate(state.getSymbolsTable(), state.getHeapTable());

        if(!value.getType().equals(new StringType()))
            throw new MyException("The expression must be a StringType!");

        StringValue fileName = (StringValue) value;

        if(state.getFileTable().isDefined(fileName.getValue()))
            throw new MyException("The file is already opened!");

        BufferedReader bufferedReader;

        try{
            bufferedReader = new BufferedReader(new FileReader(fileName.getValue()));
        } catch (FileNotFoundException exception){
            throw new MyException(fileName + " file could not be opened! ");
        }

        MyiDictionary<String, BufferedReader> fileTable = state.getFileTable();
        fileTable.addSymbol(fileName.getValue(), bufferedReader);
        state.setFileTable(fileTable);

        return null;

    }

    public IStatement createDeepCopy(){
        return new OpenReadFileStatement(expression.createDeepCopy());
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        if (!(this.expression.typeCheck(typesTable).equals(new StringType())))
            throw new MyException("Open ReadFile: A string expression must be provided!");

        return typesTable;
    }

    @Override
    public String toString(){
        return "OpenReadFile(" + expression.toString() + ")";
    }


}
