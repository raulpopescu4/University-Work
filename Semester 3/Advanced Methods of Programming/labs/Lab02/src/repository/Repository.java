package repository;

import exceptions.MyException;
import model.programState.ProgramState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Repository implements IRepository {

    List<ProgramState> programStates;
    String logFilePath;

    public Repository(ProgramState programState, String logFilePath){
        this.programStates = new ArrayList<>();
        this.programStates.add(programState);
        this.logFilePath = logFilePath;

        this.clearLogFile();
    }

    public List<ProgramState> getProgramStates() {
        return this.programStates;
    }

    public void setProgramStates(List<ProgramState> newProgramStates){
        this.programStates = newProgramStates;
    }

    public String getLogFilePath(){
        return this.logFilePath;
    }


    void setLogFilePath(String newLogFilePath){
        this.logFilePath = newLogFilePath;
    }


    public void logProgramStateExecution(ProgramState programState) throws MyException , IOException {
        try{
            PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(this.logFilePath, false)));

            logFile.println(programState.toString());
            logFile.close();
        }catch (IOException error) {
            throw new MyException(error.getMessage());
        }
    }

    public void clearLogFile() throws MyException {
        try{
            PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(this.logFilePath, false)));
            logFile.close();
        } catch (IOException error){
            throw new MyException(error.getMessage());
        }
    }


}
