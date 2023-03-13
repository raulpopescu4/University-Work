package model.dataStructures;

import exceptions.MyException;

import java.util.Stack;

public class MyStack<T> implements MyiStack<T>{
    Stack<T> stack;

    public MyStack(){
        stack = new Stack<>();
    }

    public boolean isEmpty(){
        return stack.isEmpty();
    }

    public T pop() throws MyException {
        if(isEmpty())
            throw new MyException("The stack is empty !");

        return stack.pop();
    }

    public void push(T element){
        stack.push(element);
    }

    @Override
    public String toString(){
        return stack.toString();
    }
}
