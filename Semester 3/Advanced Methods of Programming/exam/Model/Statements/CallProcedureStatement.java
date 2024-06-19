package Model.Statements;

import Model.Exceptions.MyException;
import Model.DataStructures.MyDictionary;
import Model.DataStructures.MyiDictionary;
import Model.DataStructures.MyiHeap;
import Model.DataStructures.MyiProceduresTable;
import Model.Expressions.ProgramExpression;
import Model.ProgramState.ProgramState;
import Model.Types.Type;
import Model.Values.Value;

import java.util.List;

public class CallProcedureStatement implements iStatement{
    String procedureName;
    List<ProgramExpression> expressions;

    public CallProcedureStatement(String procedureName, List<ProgramExpression> expressions) {
        this.procedureName = procedureName;
        this.expressions = expressions;
    }

    public ProgramState execute(ProgramState state) throws MyException {
        MyiDictionary<String, Value> symTable = state.getSymbolsTable().peek();
        MyiHeap heap = state.getHeapTable();
        MyiProceduresTable proceduresTable = state.getProceduresTable();

        if (!proceduresTable.isDefined(this.procedureName))
            throw new MyException("Procedure not defined!");

        List<String> variables = proceduresTable.lookUp(this.procedureName).getKey();
        iStatement statement = proceduresTable.lookUp(this.procedureName).getValue();

        MyiDictionary<String, Value> newSymTable = new MyDictionary<>();
        for(String var: variables) {
            int ind = variables.indexOf(var);
            newSymTable.add(var, this.expressions.get(ind).evaluate(symTable, heap));
        }

        state.getSymbolsTable().push(newSymTable);
        state.getExecutionStack().push(new ReturnStatement());
        state.getExecutionStack().push(statement);

        return null;
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }

    public iStatement createDeepCopy() {
        return new CallProcedureStatement(this.procedureName, this.expressions);
    }

    @Override
    public String toString() {
        return String.format("Call %s %s", this.procedureName, this.expressions.toString());
    }
}
