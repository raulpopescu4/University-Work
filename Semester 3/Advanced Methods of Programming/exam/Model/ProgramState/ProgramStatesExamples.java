package Model.ProgramState;

import Controller.Controller;
import Model.Exceptions.MyException;
import Model.DataStructures.MyDictionary;
import Model.DataStructures.MyProceduresTable;
import Model.DataStructures.MyiProceduresTable;
import Model.Expressions.*;
import Model.Statements.*;
import Model.Types.BoolType;
import Model.Types.IntType;
import Model.Types.ReferenceType;
import Model.Types.StringType;
import Model.Values.BoolValue;
import Model.Values.IntValue;
import Model.Values.StringValue;
import Repository.Repository;
import Repository.iRepository;
import View.RunExample;
import View.TextMenu;
import javafx.util.Pair;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// done for LAB07
public class ProgramStatesExamples {
    List<iStatement> programStatesList;

    // added for exam
    List<MyiProceduresTable> proceduresTablesList;

    public ProgramStatesExamples() {
        this.programStatesList = new ArrayList<>();

        // added for exam
        this.proceduresTablesList = new ArrayList<>();

        this.addProgramStatesExamplesToList();
    }

    private void addProgramStatesExamplesToList() {
        iStatement firstStatement = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignStatement("v", new ValueExpression(new IntValue(2))),
                        new PrintStatement(new VariableExpression("v"))));
        this.programStatesList.add(firstStatement);
        this.proceduresTablesList.add(new MyProceduresTable());

        iStatement secondStatement = new CompoundStatement(new VariableDeclarationStatement("a", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("b", new IntType()),
                    new CompoundStatement(new AssignStatement("a", new ArithmeticExpression('+', new ValueExpression(new IntValue(2)),
                        new ArithmeticExpression('*', new ValueExpression(new IntValue(3)), new ValueExpression(new IntValue(5))))),
                            new CompoundStatement(new AssignStatement("b", new ArithmeticExpression('+', new VariableExpression("a"),
                                new ValueExpression(new IntValue(1)))), new PrintStatement(new VariableExpression("b"))))));
        this.programStatesList.add(secondStatement);
        this.proceduresTablesList.add(new MyProceduresTable());

        iStatement thirdStatement = new CompoundStatement(new VariableDeclarationStatement("a", new BoolType()),
                new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                    new CompoundStatement(new AssignStatement("a", new ValueExpression(new BoolValue(true))),
                        new CompoundStatement(new IfStatement(new VariableExpression("a"),
                            new AssignStatement("v", new ValueExpression(new IntValue(2))),
                                new AssignStatement("v", new ValueExpression(new IntValue(3)))),
                                    new PrintStatement(new VariableExpression("v"))))));
        this.programStatesList.add(thirdStatement);
        this.proceduresTablesList.add(new MyProceduresTable());

        iStatement fourthStatement = new CompoundStatement(new VariableDeclarationStatement("varf", new StringType()),
                new CompoundStatement(new AssignStatement("varf", new ValueExpression(new StringValue("test.in"))),
                    new CompoundStatement(new OpenReadFileStatement(new VariableExpression("varf")),
                        new CompoundStatement(new VariableDeclarationStatement("varc", new IntType()),
                            new CompoundStatement(new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                new CompoundStatement(new PrintStatement(new VariableExpression("varc")),
                                    new CompoundStatement(new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                        new CompoundStatement(new PrintStatement(new VariableExpression("varc")),
                                            new CloseReadFileStatement(new VariableExpression("varf"))))))))));
        this.programStatesList.add(fourthStatement);
        this.proceduresTablesList.add(new MyProceduresTable());

        iStatement fifthStatement = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new HeapAllocationStatement("v", new ValueExpression(new IntValue(20))),
                    new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new ReferenceType(new IntType()))),
                        new CompoundStatement(new HeapAllocationStatement("a", new VariableExpression("v")),
                            new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                (new PrintStatement(new VariableExpression("a"))))))));
        this.programStatesList.add(fifthStatement);
        this.proceduresTablesList.add(new MyProceduresTable());

        iStatement sixthStatement = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new HeapAllocationStatement("v", new ValueExpression(new IntValue(20))),
                    new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new ReferenceType(new IntType()))),
                        new CompoundStatement(new HeapAllocationStatement("a", new VariableExpression("v")),
                            new CompoundStatement(new PrintStatement(new HeapReadingExpression(new VariableExpression("v"))),
                                (new PrintStatement(new ArithmeticExpression('+',
                                    new HeapReadingExpression(new HeapReadingExpression(new VariableExpression("a"))),
                                        new ValueExpression(new IntValue(5))))))))));
        this.programStatesList.add(sixthStatement);
        this.proceduresTablesList.add(new MyProceduresTable());

        iStatement seventhStatement = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new HeapAllocationStatement("v", new ValueExpression(new IntValue(20))),
                    new CompoundStatement(new PrintStatement(new HeapReadingExpression(new VariableExpression("v"))),
                        new CompoundStatement(new HeapWritingStatement("v", new ValueExpression(new IntValue(30))),
                            new PrintStatement(new ArithmeticExpression('+', new HeapReadingExpression(new VariableExpression("v")),
                                new ValueExpression(new IntValue(5))))))));
        this.programStatesList.add(seventhStatement);
        this.proceduresTablesList.add(new MyProceduresTable());

        iStatement eighthStatement = new CompoundStatement(new VariableDeclarationStatement("v", new ReferenceType(new IntType())),
                new CompoundStatement(new HeapAllocationStatement("v", new ValueExpression(new IntValue(20))),
                    new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new ReferenceType(new IntType()))),
                        new CompoundStatement(new HeapAllocationStatement("a", new VariableExpression("v")),
                            new CompoundStatement(new HeapAllocationStatement("v", new ValueExpression(new IntValue(30))),
                                (new PrintStatement(new HeapReadingExpression(new HeapReadingExpression(new VariableExpression("a"))))))))));
        this.programStatesList.add(eighthStatement);
        this.proceduresTablesList.add(new MyProceduresTable());

        iStatement ninthStatement = new CompoundStatement(new VariableDeclarationStatement("v",new IntType()),
                new CompoundStatement(new AssignStatement("v", new ValueExpression(new IntValue(4))),
                    new WhileStatement(new RelationalExpression(">", new VariableExpression("v"),
                        new ValueExpression(new IntValue(0))), new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                            new AssignStatement( "v", new ArithmeticExpression('-', new VariableExpression("v"),
                                new ValueExpression(new IntValue(1))))))));
        this.programStatesList.add(ninthStatement);
        this.proceduresTablesList.add(new MyProceduresTable());

        iStatement tenthStatement = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("a", new ReferenceType(new IntType())),
                    new CompoundStatement(new AssignStatement("v", new ValueExpression(new IntValue(10))),
                        new CompoundStatement(new HeapAllocationStatement("a", new ValueExpression(new IntValue(22))),
                            new CompoundStatement(new CreateThreadStatement(new CompoundStatement(new HeapWritingStatement("a",
                                new ValueExpression(new IntValue(30))), new CompoundStatement(
                                    new AssignStatement("v", new ValueExpression(new IntValue(32))),
                                        new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                            new PrintStatement(new HeapReadingExpression(new VariableExpression("a"))))))),
                                                new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                                    new PrintStatement(new HeapReadingExpression(new VariableExpression("a")))))))));
        this.programStatesList.add(tenthStatement);
        this.proceduresTablesList.add(new MyProceduresTable());

        // added for exam
        MyiProceduresTable eleventhStatementProceduresTable = new MyProceduresTable();

        iStatement sumProcedure = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignStatement("v", new ArithmeticExpression('+',
                    new VariableExpression("a"), new VariableExpression("b"))), new PrintStatement(new VariableExpression("v"))));

        List<String> variableSumProcedure = new ArrayList<>();
        variableSumProcedure.add("a");
        variableSumProcedure.add("b");

        eleventhStatementProceduresTable.add("sum", new Pair<>(variableSumProcedure, sumProcedure));

        iStatement productProcedure = new CompoundStatement(new VariableDeclarationStatement("v" , new IntType()),
                new CompoundStatement(new AssignStatement("v", new ArithmeticExpression('*',
                    new VariableExpression("a"), new VariableExpression("b"))), new PrintStatement(new VariableExpression("v"))));

        List<String> variablesProductProcedure = new ArrayList<>();
        variablesProductProcedure.add("a");
        variablesProductProcedure.add("b");

        eleventhStatementProceduresTable.add("product", new Pair<>(variablesProductProcedure, productProcedure));

        iStatement eleventhStatement = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("w", new IntType()),
                    new CompoundStatement(new AssignStatement("v", new ValueExpression(new IntValue(2))),
                        new CompoundStatement(new AssignStatement("w", new ValueExpression(new IntValue(5))),
                            new CompoundStatement(new CallProcedureStatement("sum", new ArrayList<>(Arrays.asList(new ArithmeticExpression('*',
                                new VariableExpression("v"), new ValueExpression(new IntValue(10))), new VariableExpression("w")))),
                                    new CompoundStatement(new PrintStatement(new VariableExpression("v")),
                                        new CreateThreadStatement(new CompoundStatement(new CallProcedureStatement("product",
                                            new ArrayList<>(Arrays.asList(new VariableExpression("v"), new VariableExpression("w")))),
                                                new CreateThreadStatement(new CallProcedureStatement("sum",
                                                    new ArrayList<>(Arrays.asList(new VariableExpression("v"), new VariableExpression("w")))))))))))));
        this.programStatesList.add(eleventhStatement);
        this.proceduresTablesList.add(eleventhStatementProceduresTable);

        // int v; v=5; if (v==5), then (int a; a=7;), else (print(v)); print(a)
        iStatement firstFaultyStatement = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignStatement("v", new ValueExpression(new IntValue(5))),
                    new CompoundStatement(new IfStatement(new RelationalExpression("==", new VariableExpression("v"),
                        new ValueExpression(new IntValue(5))), new CompoundStatement(
                            new VariableDeclarationStatement("a", new IntType()), new AssignStatement("a", new ValueExpression(new IntValue(7)))),
                                new PrintStatement(new VariableExpression("v"))), new PrintStatement(new VariableExpression("a")))));
        this.programStatesList.add(firstFaultyStatement);
        this.proceduresTablesList.add(new MyProceduresTable());

        // int v; v=6; while (v > 1) {int a; a=v; print(a); v=v-1; }; print(a);
        iStatement secondFaultyStatement = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignStatement("v", new ValueExpression(new IntValue(6))),
                    new CompoundStatement(new WhileStatement(new RelationalExpression(">", new VariableExpression("v"), new ValueExpression(new IntValue(1))),
                        new CompoundStatement(new VariableDeclarationStatement("a", new IntType()),
                            new CompoundStatement(new AssignStatement("a", new VariableExpression("v")),
                                new CompoundStatement(new PrintStatement(new VariableExpression("a")),
                                    new AssignStatement( "v", new ArithmeticExpression('-',
                                        new VariableExpression("v"), new ValueExpression(new IntValue(1)))))))),
                                            new PrintStatement(new VariableExpression("a")))));
        this.programStatesList.add(secondFaultyStatement);
        this.proceduresTablesList.add(new MyProceduresTable());

        // int v; v=7; createThread(int a; a=v;); print(a);
        iStatement thirdFaultyStatement = new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(new AssignStatement("v", new ValueExpression(new IntValue(7))),
                    new CompoundStatement(new CreateThreadStatement(new CompoundStatement(
                        new VariableDeclarationStatement("a", new IntType()), new AssignStatement("a",
                            new VariableExpression("v")))), new PrintStatement(new VariableExpression("a")))));
        this.programStatesList.add(thirdFaultyStatement);
        this.proceduresTablesList.add(new MyProceduresTable());
    }

    public List<iStatement> getProgramStatesList() {
        return this.programStatesList;
    }

    public List<MyiProceduresTable> getProceduresTablesList() {
        return this.proceduresTablesList;
    }

    public void addAllExamplesToMenu(TextMenu menu) {
        for (int index = 0; index < this.programStatesList.size(); index++) {
            iStatement eachStatement = this.programStatesList.get(index);

            // added for exam
            MyiProceduresTable eachProceduresTable = this.proceduresTablesList.get(index);

            try {
                eachStatement.typeCheck(new MyDictionary<>());

                ProgramState state = new ProgramState(eachStatement, eachProceduresTable);
                iRepository repository = new Repository(state, "log" + (index + 1) + ".txt");
                Controller controller = new Controller(repository, true);

                menu.addCommand(new RunExample(String.valueOf(index + 1), eachStatement.toString(), controller));
            } catch (MyException error) {
                System.out.println(eachStatement + " has not been created -> " + error.getMessage());
            }
        }
    }
}
