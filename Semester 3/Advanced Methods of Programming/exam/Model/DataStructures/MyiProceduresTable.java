package Model.DataStructures;

import Model.Exceptions.MyException;
import Model.Statements.iStatement;
import javafx.util.Pair;

import java.util.HashMap;
import java.util.List;
import java.util.Set;

public interface MyiProceduresTable {
    boolean isDefined(String key);

    Pair<List<String>, iStatement> lookUp(String key) throws MyException;

    void add(String key, Pair<List<String>, iStatement> value);

    void removeByKey(String key) throws MyException;

    void update(String key,  Pair<List<String>, iStatement> value) throws MyException;

    HashMap<String,  Pair<List<String>, iStatement>> getContent();

    Set<String> getKeySet();

    MyiDictionary<String, Pair<List<String>, iStatement>> createDeepCopy() throws MyException;
}