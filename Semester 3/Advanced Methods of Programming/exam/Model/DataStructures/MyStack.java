package Model.DataStructures;

import Model.Exceptions.MyException;

import java.util.Stack;

// done for LAB02
public class MyStack<T> implements MyiStack<T>{
    Stack<T> stack;

    public MyStack() {
        this.stack = new Stack<>();
    }

    public MyStack(Stack<T> _stack) {
        this.stack = _stack;
    }

    public Stack<T> getStack() {
        return this.stack;
    }

    public boolean isEmpty() {
        return this.stack.isEmpty();
    }

    public T pop() throws MyException {
        if (isEmpty())
            throw new MyException("The stack is empty!");

        return this.stack.pop();
    }

    public void push(T newValue) {
        this.stack.push(newValue);
    }

    public T peek() throws MyException {
        if (this.stack.isEmpty())
            throw new MyException("Stack is empty!");

        return this.stack.peek();
    }

    public MyiStack<T> createDeepCopy() {
        return new MyStack<T>((Stack<T>)this.stack.clone());
    }

    @Override
    public String toString() {
        return this.stack.toString();
    }
}
