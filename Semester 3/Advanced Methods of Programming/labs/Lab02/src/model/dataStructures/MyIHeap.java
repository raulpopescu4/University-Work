package model.dataStructures;

import exceptions.MyException;
import model.values.Value;

import java.util.Map;

public interface MyIHeap{

    Map<Integer, Value> getContent();

    void setContent(Map<Integer, Value> newHeap);

    Integer addSymbol(Value value);

    Value lookUp(Integer key) throws MyException;

    void updateSymbol(Integer address, Value expressionValue);

}
