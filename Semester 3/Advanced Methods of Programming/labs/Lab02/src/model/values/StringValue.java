package model.values;

import model.types.StringType;
import model.types.Type;

import java.util.Objects;

public class StringValue implements Value{
    String value;

    public StringValue(String _value){
        value = _value;
    }

    public String getValue(){
        return value;
    }

    public boolean equals(Object another){
        if(!(another instanceof StringValue))
            return false;

        return Objects.equals(value, ((StringValue) another).getValue());
    }

    public Value createDeepCopy() {
        return new StringValue(this.value);
    }

    public Type getType(){
        return new StringType();
    }

    @Override
    public String toString(){
        return String.valueOf(value);
    }

}
