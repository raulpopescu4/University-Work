package model.programState;

public class StateID {
    static int id = 0;

    public synchronized static int getID(){
        id++;
        return id;
    }

    public synchronized static void setID(int _id){
        id = _id;
    }
}
