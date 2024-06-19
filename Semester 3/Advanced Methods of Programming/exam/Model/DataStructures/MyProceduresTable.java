package Model.DataStructures;

import Model.Exceptions.MyException;
import Model.Statements.iStatement;
import javafx.util.Pair;

import java.util.HashMap;
import java.util.List;
import java.util.Set;

public class MyProceduresTable implements MyiProceduresTable{
    HashMap<String, Pair<List<String>, iStatement>> proceduresTable;

    public MyProceduresTable() {
        this.proceduresTable = new HashMap<>();
    }

    public synchronized boolean isDefined(String key) {
        return this.proceduresTable.containsKey(key);
    }

    public synchronized Pair<List<String>, iStatement> lookUp(String key) throws MyException {
        if (!isDefined(key))
            throw new MyException(key + " is not defined.");
        return this.proceduresTable.get(key);
    }

    public synchronized void add(String key, Pair<List<String>, iStatement> value) {
        this.proceduresTable.put(key, value);
    }

    public synchronized void removeByKey(String key) throws MyException {
        if (!isDefined(key))
            throw new MyException(key + " is not defined.");

        this.proceduresTable.remove(key);
    }

    public synchronized void update(String key, Pair<List<String>, iStatement> value) throws MyException {
        if (!isDefined(key))
            throw new MyException(key + " is not defined.");

        this.proceduresTable.put(key, value);
    }

    public synchronized HashMap<String, Pair<List<String>, iStatement>> getContent() {
        return this.proceduresTable;
    }

    public synchronized Set<String> getKeySet() {
        return this.proceduresTable.keySet();
    }

    public synchronized MyiDictionary<String, Pair<List<String>, iStatement>> createDeepCopy() throws MyException {
        MyiDictionary<String, Pair<List<String>, iStatement>> toReturn = new MyDictionary<>();
        for (String key: this.getKeySet())
            try {
                toReturn.add(key, lookUp(key));
            } catch (MyException e) {
                throw new MyException(e.getMessage());
            }

        return toReturn;
    }

    @Override
    public String toString() {
        return this.proceduresTable.toString();
    }
}
