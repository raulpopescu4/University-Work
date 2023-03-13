package model.statements;

import exceptions.MyException;
import model.programState.ProgramState;
import model.dataStructures.MyIHeap;
import model.dataStructures.MyiDictionary;
import model.dataStructures.MyiStack;
import model.expressions.ProgramExpression;
import model.types.BoolType;
import model.types.Type;
import model.values.BoolValue;
import model.values.Value;

public class WhileStatement implements IStatement{
    ProgramExpression expression;
    IStatement statement;

    public WhileStatement(ProgramExpression expression, IStatement statement){
        this.expression = expression;
        this.statement = statement;
    }

    public ProgramState execute(ProgramState state) throws MyException {
        MyiDictionary<String, Value> symbolsTable = state.getSymbolsTable();
        MyIHeap heap = state.getHeapTable();

        Value value = expression.evaluate(symbolsTable, heap);

        if(!(value.getType() instanceof BoolType))
            throw new MyException("The expression value must be of boolean type!");


        if (((BoolValue) value).getValue()){
            MyiStack<IStatement> executionStack = state.getExecutionStack();
            executionStack.push(this);
            executionStack.push(statement);
        }

        return null;
    }

    public IStatement createDeepCopy() {
        return new WhileStatement(expression.createDeepCopy(), statement.createDeepCopy());
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typesTable) throws MyException {
        Type expressionType = this.expression.typeCheck(typesTable);
        if(!expressionType.equals(new BoolType())){
            throw new MyException("While Statement: Condition is not BoolType!");
        }

        statement.typeCheck(typesTable.createDeepCopy());

        return typesTable;
    }

    @Override
    public String toString(){
        return "while(" + expression.toString() + ") " + statement.toString();
    }
}
