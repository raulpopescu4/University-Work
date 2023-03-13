package model.values;

import model.types.BoolType;
import model.types.Type;

public class BoolValue implements Value{
    boolean value;

    public BoolValue(boolean _value){
        value = _value;
    }

    public boolean getValue(){
        return value;
    }

    @Override
    public String toString(){
        if(value)
            return "True";
        else return "False";
    }

    public Type getType(){
        return new BoolType();
    }

    public boolean equals(Object another){
        if (!(another instanceof BoolValue))
            return false;

        return value == ((BoolValue) another).getValue();
    }

    public Value createDeepCopy() {
        return new BoolValue(this.value);
    }
}
