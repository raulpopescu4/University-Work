package model.dataStructures;

import exceptions.MyException;
import model.values.Value;

import java.util.HashMap;
import java.util.Map;

public class MyHeap implements MyIHeap{
    Map<Integer, Value> map;
    Integer lastOccupiedAddress;

    public MyHeap(){
        map = new HashMap<>();
        lastOccupiedAddress = 0;
    }


    public Map<Integer, Value> getContent() {
        return map;
    }

    public void setContent(Map<Integer, Value> newHeap) {
        this.map = newHeap;
    }

    public Integer addSymbol(Value value) {
        lastOccupiedAddress += 1;
        map.put(lastOccupiedAddress, value);

        return lastOccupiedAddress;
    }

    public boolean isDefined(Integer address){
        return map.containsKey(address);
    }


    public Value lookUp(Integer address) throws MyException {
        if(!isDefined(address))
            throw new MyException("There is no value for the key " + address.toString() + "!");

        return map.get(address);
    }

    public void updateSymbol(Integer address, Value expressionValue) {
        if (!map.containsKey(address))
            throw new MyException(address.toString() + " is not present in the heap!");

        map.put(address, expressionValue);
    }

    @Override
    public String toString(){
        return map.toString();
    }
}
