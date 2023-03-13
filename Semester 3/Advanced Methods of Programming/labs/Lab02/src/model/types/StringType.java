package model.types;

import model.values.StringValue;
import model.values.Value;

public class StringType implements Type{

    public Value getDefaultValue() {
        return new StringValue("");
    }

    public boolean equals(Object another){
        return another instanceof StringType;
    }

    @Override
    public String toString(){
        return "string";
    }

    


}
