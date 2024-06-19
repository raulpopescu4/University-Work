package Model.Statements;

import Model.Exceptions.MyException;
import Model.DataStructures.MyiDictionary;
import Model.ProgramState.ProgramState;
import Model.Types.Type;

// added for exam
public class ReturnStatement implements iStatement{
    public ProgramState execute(ProgramState state) throws MyException {
        state.getSymbolsTable().pop();
        return null;
    }

    public MyiDictionary<String, Type> typeCheck(MyiDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }

    public iStatement createDeepCopy() {
        return new ReturnStatement();
    }

    @Override
    public String toString() {
        return "Return";
    }
}
