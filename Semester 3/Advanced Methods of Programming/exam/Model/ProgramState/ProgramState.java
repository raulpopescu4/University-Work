package Model.ProgramState;

import Model.Exceptions.MyException;
import Model.DataStructures.*;
import Model.Statements.iStatement;
import Model.Values.Value;

import java.io.BufferedReader;

// done for LAB07
public class ProgramState {
    int id;
    MyiStack<iStatement> executionStack;
    MyiStack<MyiDictionary<String, Value>> symbolsTable;
    MyiList<Value> outputValues;
    MyiDictionary<String, BufferedReader> fileTable;
    MyiHeap heapTable;

    // added for exam
    MyiProceduresTable proceduresTable;
    iStatement originalProgram;

    public ProgramState(iStatement _program) {
        this.id = StateID.getID();

        this.executionStack = new MyStack<>();

        this.symbolsTable = new MyStack<>();
        // added for exam
        this.symbolsTable.push(new MyDictionary<>());

        this.outputValues = new MyList<>();
        this.fileTable = new MyDictionary<>();
        this.heapTable = new MyHeap();

        // added for exam
        this.proceduresTable = new MyProceduresTable();

        this.originalProgram = _program.createDeepCopy();

        this.executionStack.push(this.originalProgram);
    }

    // added for exam
    public ProgramState(iStatement _program, MyiProceduresTable _proceduresTable) {
        this.id = StateID.getID();

        this.executionStack = new MyStack<>();

        this.symbolsTable = new MyStack<>();
        // added for exam
        this.symbolsTable.push(new MyDictionary<>());

        this.outputValues = new MyList<>();
        this.fileTable = new MyDictionary<>();
        this.heapTable = new MyHeap();

        // added for exam
        this.proceduresTable = _proceduresTable;

        this.originalProgram = _program.createDeepCopy();

        this.executionStack.push(this.originalProgram);
    }

    public ProgramState(iStatement _program, MyiStack<iStatement> _stack, MyiStack<MyiDictionary<String,Value>> _symbolsTable, MyiList<Value> _outputValues, MyiDictionary<String, BufferedReader> _fileTable, MyiHeap _heapTable, MyiProceduresTable _proceduresTable) {
        this.id = StateID.getID();

        this.executionStack = _stack;
        this.symbolsTable = _symbolsTable;
        this.outputValues = _outputValues;
        this.fileTable = _fileTable;
        this.heapTable = _heapTable;

        // added for exam
        this.proceduresTable = _proceduresTable;

        this.originalProgram = _program.createDeepCopy();

        this.executionStack.push(this.originalProgram);
    }

    public MyiStack<iStatement> getExecutionStack() {
        return this.executionStack;
    }

    public MyiStack<MyiDictionary<String,Value>> getSymbolsTable() {
        return this.symbolsTable;
    }

    public MyiDictionary<String, Value> getTopOfSymbolsTable() {
        try {
            return this.symbolsTable.peek();
        } catch (MyException e) {
            System.out.println("Stack is empty!");
            return null;
        }
    }

    public MyiList<Value> getOutputValues() {
        return this.outputValues;
    }

    public MyiDictionary<String, BufferedReader> getFileTable() { return this.fileTable; }

    public MyiHeap getHeapTable() {
        return this.heapTable;
    }

    public MyiProceduresTable getProceduresTable() { return this.proceduresTable; }

    public iStatement getOriginalProgram() {
        return this.originalProgram;
    }

    public int getID() {
        return this.id;
    }

    public void setExecutionStack(MyiStack<iStatement> newExecutionStack) {
        this.executionStack = newExecutionStack;
    }

    public void setSymbolsTable(MyiStack<MyiDictionary<String,Value>> newSymbolsTable) {
        this.symbolsTable = newSymbolsTable;
    }

    public void setOutputValues(MyiList<Value> newOutputValues) {
        this.outputValues = newOutputValues;
    }

    public void setFileTable(MyiDictionary<String, BufferedReader> newFileTable) {
        this.fileTable = newFileTable;
    }

    public void setHeapTable(MyiHeap newHeapTable) {
        this.heapTable = newHeapTable;
    }

    public void setProceduresTable(MyiProceduresTable newProceduresTable) { this.proceduresTable = newProceduresTable;}

    public void setOriginalProgram(iStatement newOriginalProgram){
        this.originalProgram = newOriginalProgram;
    }

    public void setID(int newID) {
        this.id = newID;
    }

    public Boolean isNotCompleted() {
        return !this.executionStack.isEmpty();
    }

    public ProgramState oneStepExecution() throws MyException {
        if(this.executionStack.isEmpty())
            throw new MyException("ProgramState's stack is empty!");

        iStatement currentStatement = this.executionStack.pop();

        return currentStatement.execute(this);
    }

    @Override
    public String toString() {
        return "Program state ID: " + this.id + "\nExecution stack: \n" + this.executionStack.toString() +
                "\nSymbols tables: \n" + this.symbolsTable.toString() + "\nOutput values: \n" + this.outputValues.toString() +
                "\nFile table: \n" + this.fileTable.toString()  + "\nHeap table: \n" + this.heapTable.toString() +
                "\nProcedures table: \n" + this.proceduresTable.toString();
    }
}
