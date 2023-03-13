package model.dataStructures;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements MyiList<T>{
    List<T> list;

    public MyList(){
        list = new ArrayList<>();
    }

    public void add(T element){
        list.add(element);
    }

    @Override
    public String toString(){
        return list.toString();
    }

}
