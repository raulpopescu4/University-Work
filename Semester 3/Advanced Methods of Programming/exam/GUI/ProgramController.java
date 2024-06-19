package GUI;

import Controller.Controller;

import java.io.BufferedReader;
import java.util.*;

import Model.Exceptions.MyException;
import Model.DataStructures.MyiProceduresTable;
import Model.ProgramState.ProgramState;
import Model.Statements.iStatement;
import Model.Values.Value;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleObjectProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.ListView;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TextField;
import javafx.scene.control.TableView;

public class ProgramController {
    private Controller controller;

    public void setController(Controller controller) {
        this.controller = controller;
        this.populate();
    }

    @FXML
    private TableView<Map.Entry<Integer, Value>> heapTableView;

    @FXML
    private TableColumn<Map.Entry<Integer, Value>, Integer> heapAddressColumn;

    @FXML
    private TableColumn<Map.Entry<Integer, Value>, String> heapValueColumn;

    @FXML
    private ListView<String> fileListView;

    @FXML
    private TableView<Map.Entry<String, Value>> symbolTableView;

    @FXML
    private TableColumn<Map.Entry<String, Value>, String> symbolTableVariableColumn;

    @FXML
    private TableColumn<Map.Entry<String, Value>, String> symbolTableValueColumn;

    @FXML
    private ListView<String> outputListView;

    @FXML
    private ListView<Integer> programStateListView;

    @FXML
    private ListView<String> executionStackListView;

    @FXML
    private TextField numberOfProgramStatesTextField;

    // added for exam
    @FXML
    private TableView<Map.Entry<String, javafx.util.Pair<List<String>, iStatement>>> procedureTableView;

    @FXML
    private TableColumn<Map.Entry<String, javafx.util.Pair<List<String>, iStatement>>, javafx.util.Pair<String, List<String>>> procedureNameTableColumn;

    @FXML
    private TableColumn<Map.Entry<String, javafx.util.Pair<List<String>, iStatement>>, String> procedureBodyTableColumn;

    @FXML
    private Button executeOneStepButton;

    public void initialize() {
        this.heapAddressColumn.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().getKey()).asObject());
        this.heapValueColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getValue().toString()));

        this.symbolTableVariableColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getKey() + ""));
        this.symbolTableValueColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getValue().toString()));

        // added for exam
        this.procedureNameTableColumn.setCellValueFactory(p -> new SimpleObjectProperty<>(new javafx.util.Pair<>(p.getValue().getKey(), p.getValue().getValue().getKey())));
        this.procedureBodyTableColumn.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().getValue().getValue().toString()));

        this.numberOfProgramStatesTextField.setEditable(false);

        this.executeOneStepButton.setOnAction((ActionEvent event) -> {
            if (this.controller == null) {
                Alert alert = new Alert(Alert.AlertType.ERROR, "No program was selected!", ButtonType.OK);
                alert.setTitle("Program not found!");
                alert.showAndWait();
                return;
            }

            boolean programStateLeft;

            if (this.getCurrentProgramState() == null)
                programStateLeft = false;
            else
                programStateLeft = this.getCurrentProgramState().getExecutionStack().isEmpty();

            if(programStateLeft) {
                Alert alert = new Alert(Alert.AlertType.ERROR, "Nothing left to execute!", ButtonType.OK);
                alert.setTitle("Execution stack empty!");
                alert.showAndWait();
            }

            try {
                this.controller.oneStepExecution();
                this.populate();
            } catch (MyException error) {
                Alert alert = new Alert(Alert.AlertType.ERROR, error.getMessage(), ButtonType.OK);
                alert.showAndWait();
            }
        });

        this.programStateListView.setOnMouseClicked(mouseEvent -> this.populate());
    }

    private ProgramState getCurrentProgramState() {
        if (this.controller == null)
            return null;

        if (this.controller.getProgramStates().size() == 0)
            return null;

        List<ProgramState> programStateList = this.controller.getProgramStates();
        int selectedIndex = this.programStateListView.getSelectionModel().getSelectedIndex();
        if (selectedIndex < 0 || selectedIndex >= programStateList.size())
            return programStateList.get(0);

        return programStateList.get(selectedIndex);
    }

    private void populate() {
        this.populateHeapTableView();
        this.populateOutputListView();
        this.populateFileTableView();
        this.populateProgramStateIDsListView();
        this.populateSymbolsTableView();
        this.populateExecutionStackListView();

        // added for exam
        this.populateProcedureTableView();
    }

    private void populateExecutionStackListView() {
        ProgramState programState = this.getCurrentProgramState();
        List<String> executionStackString = new ArrayList<>();

        if (programState != null)
            for (iStatement statement : programState.getExecutionStack().getStack())
                executionStackString.add(statement.toString());

        this.executionStackListView.setItems(FXCollections.observableList(executionStackString));
        this.executionStackListView.refresh();
    }

    private void populateSymbolsTableView() {
        ProgramState programState = this.getCurrentProgramState();
        List<Map.Entry<String, Value>> symbolTableList = new ArrayList<>();

        if (programState != null)
            for(Map.Entry<String, Value> entry : programState.getTopOfSymbolsTable().getContent().entrySet())
                symbolTableList.add(Map.entry(entry.getKey(), entry.getValue()));

        this.symbolTableView.setItems(FXCollections.observableList(symbolTableList));
        this.symbolTableView.refresh();
    }

    private void populateOutputListView() {
        ProgramState programState = this.getCurrentProgramState();
        List<String> outputTableList = new ArrayList<>();

        if (programState != null)
            for(Value entry : programState.getOutputValues().getList())
                outputTableList.add(entry.toString());

        this.outputListView.setItems(FXCollections.observableList(outputTableList));
        this.outputListView.refresh();
    }

    private void populateFileTableView() {
        ProgramState programState = this.getCurrentProgramState();
        List<String> fileTableList = new ArrayList<>();

        if (programState != null)
            for(Map.Entry<String, BufferedReader> entry : programState.getFileTable().getContent().entrySet())
                fileTableList.add(entry.getKey());

        this.fileListView.setItems(FXCollections.observableList(fileTableList));
        this.fileListView.refresh();
    }

    private void populateHeapTableView() {
        ProgramState programState = this.getCurrentProgramState();
        List<Map.Entry<Integer, Value>> heapTableList = new ArrayList<>();

        if (programState != null)
            for(Map.Entry<Integer, Value> entry : programState.getHeapTable().getContent().entrySet())
                heapTableList.add(Map.entry(entry.getKey(), entry.getValue()));

        this.heapTableView.setItems(FXCollections.observableList(heapTableList));
        this.heapTableView.refresh();
    }

    private void populateProgramStateIDsListView() {
        List<Integer> programStatesIDsList = new ArrayList<>();

        if (this.controller != null) {
            List<ProgramState> programStatesList = this.controller.getProgramStates();
            programStatesIDsList = programStatesList.stream().map(ProgramState::getID).toList();
        }

        this.programStateListView.setItems(FXCollections.observableList(programStatesIDsList));
        this.programStateListView.refresh();

        this.populateNumberOfProgramStatesTextField();
    }

    private void populateNumberOfProgramStatesTextField() {
        List<ProgramState> programStatesList = this.controller.getProgramStates();
        int numberOfProgramStates = programStatesList.size();

        this.numberOfProgramStatesTextField.setText(String.valueOf(numberOfProgramStates));
    }

    private void populateProcedureTableView() {
        ProgramState programState = this.getCurrentProgramState();
        List<Map.Entry<String, javafx.util.Pair<List<String>, iStatement>>> proceduresTableList = new ArrayList<>();

        if (programState != null) {
            MyiProceduresTable proceduresTable = programState.getProceduresTable();

            for (Map.Entry<String, javafx.util.Pair<List<String>, iStatement>> entry : proceduresTable.getContent().entrySet()) {
                Map.Entry<String, javafx.util.Pair<List<String>, iStatement>> eachEntry = new AbstractMap.SimpleEntry<>(entry.getKey(), entry.getValue());
                proceduresTableList.add(eachEntry);
            }
        }

        this.procedureTableView.setItems(FXCollections.observableList(proceduresTableList));
        this.procedureTableView.refresh();
    }

}