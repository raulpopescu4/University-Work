package model.programState;

import exceptions.MyException;
import model.dataStructures.*;
import model.statements.IStatement;
import model.values.Value;

import java.io.BufferedReader;

public class ProgramState {
    int id;
    MyiStack<IStatement> executionStack;
    MyiList<Value> outputValues;
    MyiDictionary<String, Value> symbolsTable;
    MyiDictionary<String, BufferedReader> fileTable;

    MyIHeap heapTable;

    IStatement originalProgram;

    public ProgramState(IStatement _program){
        id = StateID.getID();
        executionStack = new MyStack<>();
        symbolsTable = new MyDictionary<>();
        outputValues = new MyList<>();
        fileTable = new MyDictionary<>();
        heapTable = new MyHeap();

        originalProgram = _program.createDeepCopy();

        executionStack.push(originalProgram);
    }

    public ProgramState(IStatement program, MyiStack<IStatement> stack, MyiDictionary<String, Value> symbolsTable, MyiList<Value> outputValues, MyiDictionary<String, BufferedReader> fileTable, MyIHeap heapTable) {
        this.id = StateID.getID();

        this.executionStack = stack;
        this.symbolsTable = symbolsTable;
        this.outputValues = outputValues;
        this.fileTable = fileTable;
        this.heapTable = heapTable;

        this.originalProgram = program.createDeepCopy();

        this.executionStack.push(this.originalProgram);
    }

    public IStatement getOriginalProgram(){
        return this.originalProgram;
    }

    public MyiStack<IStatement> getExecutionStack() {
        return executionStack;
    }

    public MyiList<Value> getOutputValues(){
        return outputValues;
    }


    public MyiDictionary<String, Value> getSymbolsTable() {
        return symbolsTable;
    }

    public void setOutputValues(MyiList<Value> newOutputValues) {
        outputValues = newOutputValues;
    }

    public void setExecutionStack(MyiStack<IStatement> newExecutionStack) {
        executionStack = newExecutionStack;
    }

    public void setSymbolsTable(MyiDictionary<String, Value> newSymbolsTable) {
        symbolsTable = newSymbolsTable;
    }


    public MyiDictionary<String, BufferedReader> getFileTable(){ return fileTable;}

    public void setFileTable(MyiDictionary<String, BufferedReader> newFileTable){ fileTable = newFileTable;}

    public void resetToOriginalProgram() {
        executionStack = new MyStack<>();
        symbolsTable = new MyDictionary<>();
        outputValues = new MyList<>();
        heapTable = new MyHeap();

        executionStack.push(originalProgram.createDeepCopy());
    }

    @Override
    public String toString(){
        return "Program state ID: " + this.id +"\nExecution stack: \n" + executionStack.toString() + "\nSymbols table: \n" + symbolsTable.toString() + "\nOutput values: \n" + outputValues.toString() + "\nFile table: \n" + fileTable.toString() + "\nHeap Table: \n" + heapTable.toString();
    }

    public MyIHeap getHeapTable() {
        return heapTable;
    }

    public void setHeapTable(MyIHeap newHeapTable){ heapTable = newHeapTable;}

    public Boolean isNotCompleted(){
        return !this.executionStack.isEmpty();
    }

    public ProgramState oneStep() throws MyException{
        if(executionStack.isEmpty())
            throw new MyException("ProgramState's stack is empty!");

        IStatement currentStatement = this.executionStack.pop();

        return currentStatement.execute(this);
    }
}
