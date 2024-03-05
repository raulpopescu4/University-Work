package Model.DataStructures;

import Model.Exceptions.MyException;

import java.util.Stack;

// done for LAB02
public interface MyiStack<T> {
    T pop() throws MyException;

    void push(T newValue);

    T peek() throws MyException;

    boolean isEmpty();

    Stack<T> getStack();

    MyiStack<T> createDeepCopy();
}