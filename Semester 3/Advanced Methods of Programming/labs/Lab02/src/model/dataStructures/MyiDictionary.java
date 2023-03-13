package model.dataStructures;

import java.util.HashMap;
import java.util.Map;

public interface MyiDictionary <T1, T2>{
    boolean isDefined(T1 key);

    T2 lookUp(T1 key);

    void addSymbol(T1 key, T2 value);

    void update(T1 key, T2 value);

    void removeSymbol(T1 key);

    HashMap<T1, T2> getContent();

    MyiDictionary<T1, T2> createDeepCopy();
}
