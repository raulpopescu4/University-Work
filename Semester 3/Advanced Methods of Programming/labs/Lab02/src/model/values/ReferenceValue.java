package model.values;

import model.types.ReferenceType;
import model.types.Type;

public class ReferenceValue implements Value{

    int address;
    Type locationType;

    public Type getType() {
        return new ReferenceType(locationType);
    }

    public Value createDeepCopy() {
        return new ReferenceValue(this.address, this.locationType);
    }

    public ReferenceValue(int address, Type locationType){
        this.address = address;
        this.locationType = locationType;
    }

    public int getAddress(){
        return address;
    }

    public Type getLocationType(){
        return locationType;
    }

    @Override
    public String toString(){
        return locationType.toString() + "* " + String.valueOf(address);
    }

}
