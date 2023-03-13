package model.values;

import model.types.IntType;
import model.types.Type;

public class IntValue implements Value{
    int value;

    public IntValue(int _value){
        value = _value;
    }

    public int getValue(){
        return value;
    }

    public Type getType(){
        return new IntType();
    }

    @Override
    public String toString(){
        return String.valueOf(value);
    }

    public boolean equals(Object another){
        if(!(another instanceof IntValue))
            return false;

        return value == ((IntValue) another).getValue();
    }

    public Value createDeepCopy() {
        return new IntValue(this.value);
    }

}
