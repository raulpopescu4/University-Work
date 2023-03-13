package repository;

import exceptions.MyException;
import model.programState.ProgramState;

import java.io.IOException;
import java.util.List;

public interface IRepository {
    List<ProgramState> getProgramStates();

    void setProgramStates(List<ProgramState> newProgramState);

    String getLogFilePath();

    void logProgramStateExecution(ProgramState programState) throws MyException, IOException;

    void clearLogFile() throws MyException;

}
