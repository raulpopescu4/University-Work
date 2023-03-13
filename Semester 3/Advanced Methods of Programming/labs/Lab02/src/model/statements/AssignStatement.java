package model.statements;

import exceptions.MyException;
import model.dataStructures.MyiDictionary;
import model.dataStructures.MyiStack;
import model.expressions.ProgramExpression;
import model.programState.ProgramState;
import model.types.Type;
import model.values.Value;

public class AssignStatement implements IStatement {
    String id;
    ProgramExpression expression;

    public AssignStatement(String _id, ProgramExpression _expression){
        id = _id;
        expression = _expression;

    }

    public ProgramState execute(ProgramState state) throws MyException {
        MyiStack<IStatement> stack = state.getExecutionStack();
        MyiDictionary<String, Value> symbolTable = state.getSymbolsTable();

        if (symbolTable.isDefined(id)){
            Value value = expression.evaluate(symbolTable, state.getHeapTable());
            Type idType = (symbolTable.lookUp(id).getType());
            if(value.getType().equals(idType))
                symbolTable.update(id, value);
            else throw new MyException("declared type of variable" + id + " and type of the assigned expression do not match");


        }
        else throw new MyException("the used variable" + id + "was not declared before");

        return null;
    }

    public IStatement createDeepCopy() {
        return new AssignStatement(id, expression.createDeepCopy());
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        Type variableType = typesTable.lookUp(this.id);
        Type expressionType = expression.typeCheck(typesTable);
        if (variableType.equals(expressionType)){
            return typesTable;
        } else
            throw new MyException("Assignment Statement: right hand side and left side have different types!");

    }

    @Override
    public String toString(){
        return id + " = " + expression.toString();
    }


}
