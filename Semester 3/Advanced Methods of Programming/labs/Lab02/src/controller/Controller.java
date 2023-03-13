package controller;

import exceptions.MyException;
import model.dataStructures.MyiStack;
import model.programState.ProgramState;
import model.statements.IStatement;
import model.values.ReferenceValue;
import model.values.Value;
import repository.IRepository;

import java.io.IOException;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Controller {

    IRepository repository;
    boolean displayFlag = false;
    ExecutorService executor;

    public Controller(IRepository _repository, boolean _displayFlag){
        this.repository = _repository;
        this.displayFlag = _displayFlag;
    }

    public boolean getDisplayFlag(){
        return displayFlag;
    }

    public void setDisplayFlag(boolean newDisplayFlag){
        displayFlag = newDisplayFlag;
    }

    Map<Integer, Value> unsafeGarbageCollector(List<Integer> symbolsTableAddresses, Map<Integer,Value> heap) {
        return heap.entrySet().stream().filter(e-> symbolsTableAddresses.contains(e.getKey())).
                collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    Map<Integer, Value> safeGarbageCollector(List<Integer> symbolsTableAddresses, List<Integer> heapTableAddresses, Map<Integer,Value> heapTable) {
        return heapTable.entrySet().stream().filter(e-> symbolsTableAddresses.contains(e.getKey()) || heapTableAddresses.contains(e.getKey())).
                collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    List<Integer> getAddressFromTable(Collection<Value> symTableValues){
        return symTableValues.stream()
                .filter(v-> v instanceof ReferenceValue)
                .map(v-> {ReferenceValue value1 = (ReferenceValue) v; return value1.getAddress();})
                .collect(Collectors.toList());
    }


    public void oneStepForAllProgramStates(List<ProgramState> programStatesList) throws MyException{
        programStatesList.forEach(programState -> {
            try {
                this.repository.logProgramStateExecution(programState);
            } catch (IOException e) {
                throw new RuntimeException(e);
            }

            displayProgramState(programState);
        });

        List<Callable<ProgramState>> callList = programStatesList.stream().map((ProgramState programState) -> (Callable<ProgramState>) (programState::oneStep)).collect(Collectors.toList()); ;

        try{
           List<ProgramState> newProgramStatesList = executor.invokeAll(callList).stream().map(future -> {
               try{
                   return future.get();
               } catch (InterruptedException | ExecutionException error){
                   System.out.println(error.getMessage());
                   return null;
               }
           }).filter(Objects::nonNull).collect(Collectors.toList());

           programStatesList.addAll(newProgramStatesList);

           programStatesList.forEach(programState -> {
               try {
                   this.repository.logProgramStateExecution(programState);
               } catch (IOException error) {
                   throw new MyException(error.getMessage());
               }

               displayProgramState(programState);
           });

           this.repository.setProgramStates(programStatesList);


        }catch (InterruptedException error){
            throw new MyException(error.getMessage());
            }


    }


    public void allStepExecution() throws IOException {
        this.executor = Executors.newFixedThreadPool(2);

        List<ProgramState> programStatesList = removeCompletedProgramStates(this.repository.getProgramStates());

        IStatement firstStatement = this.repository.getProgramStates().get(0).getOriginalProgram();

        while(programStatesList.size() > 0){
            conservativeGarbageCollector(programStatesList);
            oneStepForAllProgramStates(programStatesList);

            programStatesList = removeCompletedProgramStates(this.repository.getProgramStates());
        }

        this.executor.shutdownNow();

        programStatesList.add(new ProgramState(firstStatement));

        this.repository.setProgramStates(programStatesList);


    }


    public void conservativeGarbageCollector(List<ProgramState> programStatesList) {

        programStatesList.forEach(programState -> {programState.getHeapTable().setContent(safeGarbageCollector(getAddressFromTable(programState.getSymbolsTable().getContent().values()),
                getAddressFromTable(programState.getHeapTable().getContent().values()), programState.getHeapTable().getContent()));});
    }

    public void displayProgramState(ProgramState programState){
        if(displayFlag)
            System.out.println(programState.toString());
    }

    public List<ProgramState> removeCompletedProgramStates(List<ProgramState> currentProgramsList){
        return currentProgramsList.stream().filter(ProgramState::isNotCompleted).collect(Collectors.toList());
    }

}
