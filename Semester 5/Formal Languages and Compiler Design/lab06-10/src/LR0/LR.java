package LR0;

import ParsingTable.ParsingTable;
import ParsingTable.RowTable;
import ParsingTree.ParserOutput;
import State.*;
import Utils.Pair;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class LR {

    private final Grammar grammar;
    private final Grammar workingGrammar;
    private List<Pair<String, List<String>>> orderedProductions;

    public LR(Grammar grammar) throws Exception {
        this.grammar = grammar;

        if (this.grammar.getIsEnriched()) {
            this.workingGrammar = this.grammar;
        } else {
            this.workingGrammar = this.grammar.getEnrichedGrammar();
        }

        orderedProductions = this.grammar.getOrderedProductions();
    }

    public String getNonTerminalPrecededByDot(Item item) {
        try {
            String term = item.getRightHandSide().get(item.getPositionForDot());
            if (!grammar.getNonTerminals().contains(term)) {
                return null;
            }

            return term;
        } catch (Exception e) {
            return null;
        }
    }

    public State closure(Item item) {
        Set<Item> oldClosure;
        Set<Item> currentClosure = Set.of(item);

        do {
            oldClosure = currentClosure;
            Set<Item> newClosure = new LinkedHashSet<>(currentClosure);
            for (Item i : currentClosure) {
                String nonTerminal = getNonTerminalPrecededByDot(i);
                if (nonTerminal != null) {
                    for (List<String> prod : grammar.getProductionsForNonTerminal(nonTerminal)) {
                        Item currentItem = new Item(nonTerminal, prod, 0);
                        newClosure.add(currentItem);
                    }
                }
            }
            currentClosure = newClosure;
        } while (!oldClosure.equals(currentClosure));

        return new State(currentClosure);
    }

    public State goTo(State state, String elem) {
        Set<Item> result = new LinkedHashSet<>();

        for (Item i : state.getItems()) {
            try {
                String nonTerminal = i.getRightHandSide().get(i.getPositionForDot());
                if (Objects.equals(nonTerminal, elem)) {
                    Item nextItem = new Item(i.getLeftHandSide(), i.getRightHandSide(), i.getPositionForDot() + 1);
                    State newState = closure(nextItem);
                    result.addAll(newState.getItems());
                }
            } catch (Exception ignored) {
            }
        }

        return new State(result);
    }

    public CanonicalCollection canonicalCollection() {
        CanonicalCollection canonicalCollection = new CanonicalCollection();

        canonicalCollection.addState(
                closure(
                        new Item(
                                workingGrammar.getStartingSymbol(),
                                workingGrammar.getProductionsForNonTerminal(workingGrammar.getStartingSymbol()).get(0),
                                0
                        )
                )
        );

        int index = 0;
        while (index < canonicalCollection.getStates().size()) {
            for (String symbol : canonicalCollection.getStates().get(index).getSymbolsSucceedingTheDot()) {
                State newState = goTo(canonicalCollection.getStates().get(index), symbol);
                if (newState.getItems().size() != 0) {
                    int indexState = canonicalCollection.getStates().indexOf(newState);
                    if (indexState == -1) {
                        canonicalCollection.addState(newState);
                        indexState = canonicalCollection.getStates().size() - 1;
                    }
                    canonicalCollection.connectStates(index, symbol, indexState);
                }
            }
            ++index;
        }
        return canonicalCollection;
    }

    public ParsingTable getParsingTable(CanonicalCollection canonicalCollection) throws Exception {
        ParsingTable parsingTable = new ParsingTable();

        for (int i = 0; i < this.canonicalCollection().getStates().size(); i++) {
            State state = this.canonicalCollection().getStates().get(i);
            RowTable row = new RowTable();
            row.stateIndex = i;
            row.action = state.getStateActionType();
            row.shifts = new ArrayList<>();

            if (state.getStateActionType() == StateActionType.SHIFT_REDUCE_CONFLICT || state.getStateActionType() == StateActionType.REDUCE_REDUCE_CONFLICT) {
                handleConflicts(i, canonicalCollection, row);
                parsingTable.entries = new ArrayList<>();
                return parsingTable;
            } else if (state.getStateActionType() == StateActionType.REDUCE) {
                handleReduceAction(state, row);
            } else if (state.getStateActionType() == StateActionType.ACCEPT) {
                handleAcceptAction(row);
            } else if (state.getStateActionType() == StateActionType.SHIFT) {
                handleShiftAction(i, canonicalCollection, row);
            }

            parsingTable.entries.add(row);
        }

        return parsingTable;
    }

    private void handleConflicts(int index, CanonicalCollection canonicalCollection, RowTable row) throws Exception {
        for (Map.Entry<Pair<Integer, String>, Integer> e2 : canonicalCollection.getAdjacencyList().entrySet()) {
            Pair<Integer, String> k2 = e2.getKey();
            Integer v2 = e2.getValue();

            if (v2.equals(row.stateIndex)) {
                printConflictInfo(index, canonicalCollection, k2, row);
                break;
            }
        }
    }

    private void printConflictInfo(int index, CanonicalCollection canonicalCollection, Pair<Integer, String> k2, RowTable row) throws Exception {
        System.out.println("STATE INDEX -> " + row.stateIndex);
        writeToFile("Input_Output/Out2.txt", "STATE INDEX -> " + row.stateIndex);
        System.out.println("SYMBOL -> " + k2.getSecond());
        writeToFile("Input_Output/Out2.txt", "SYMBOL -> " + k2.getSecond());
        System.out.println("INITIAL STATE -> " + k2.getFirst());
        writeToFile("Input_Output/Out2.txt", "INITIAL STATE -> " + k2.getFirst());
        System.out.println("( " + k2.getFirst() + ", " + k2.getSecond() + " )" + " -> " + row.stateIndex);
        writeToFile("Input_Output/Out2.txt", "( " + k2.getFirst() + ", " + k2.getSecond() + " )" + " -> " + row.stateIndex);
        System.out.println("STATE -> " + canonicalCollection.getStates().get(index));
        writeToFile("Input_Output/Out2.txt", "STATE -> " + canonicalCollection.getStates().get(index));

        throw new Exception("Conflicts found. Parsing halted.");
    }

    private void handleReduceAction(State state, RowTable row) {
        Item item = state.getItems().stream().filter(Item::dotIsLast).findAny().orElse(null);
        if (item != null) {
            row.shifts = null;
            row.reduceNonTerminal = item.getLeftHandSide();
            row.reduceContent = item.getRightHandSide();
        }
    }

    private void handleAcceptAction(RowTable row) {
        row.reduceContent = null;
        row.reduceNonTerminal = null;
        row.shifts = null;
    }

    private void handleShiftAction(int i, CanonicalCollection canonicalCollection, RowTable row) {
        List<Pair<String, Integer>> goTos = new ArrayList<>();

        for (Map.Entry<Pair<Integer, String>, Integer> entry : canonicalCollection.getAdjacencyList().entrySet()) {
            Pair<Integer, String> key = entry.getKey();
            if (key.getFirst() == row.stateIndex) {
                goTos.add(new Pair<>(key.getSecond(), entry.getValue()));
            }
        }

        row.shifts = goTos;
        row.reduceContent = null;
        row.reduceNonTerminal = null;
    }

    public void parse(Stack<String> inputStack, ParsingTable parsingTable, String filePath) throws IOException {
        Stack<Pair<String, Integer>> workingStack = new Stack<>();
        Stack<String> outputStack = new Stack<>();
        Stack<Integer> outputNumberStack = new Stack<>();

        String lastSymbol = "";
        int stateIndex = 0;

        boolean sem = true;

        workingStack.push(new Pair<>(lastSymbol, stateIndex));
        RowTable lastRow = null;
        String onErrorSymbol = null;

        try {
            do {
                if (!inputStack.isEmpty()) {
                    onErrorSymbol = inputStack.peek();
                }
                lastRow = parsingTable.entries.get(stateIndex);
                RowTable entry = parsingTable.entries.get(stateIndex);

                if (entry.action.equals(StateActionType.SHIFT)) {
                    handleShiftActionInParse(inputStack, workingStack, entry, lastSymbol, stateIndex);
                } else if (entry.action.equals(StateActionType.REDUCE)) {
                    handleReduceActionInParse(inputStack, workingStack, outputStack, outputNumberStack, lastSymbol, entry);
                } else {
                    handleAcceptActionInParse(filePath, outputStack, outputNumberStack);
                    sem = false;
                }
            } while (sem);
        } catch (NullPointerException ex) {
            handleNullPointerExceptionInParse(stateIndex, onErrorSymbol, lastRow);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private void handleShiftActionInParse(Stack<String> inputStack, Stack<Pair<String, Integer>> workingStack, RowTable entry, String lastSymbol, int stateIndex) {
        String symbol = inputStack.pop();
        Pair<String, Integer> state = entry.shifts.stream().filter(it -> it.getFirst().equals(symbol)).findAny().orElse(null);

        if (state != null) {
            stateIndex = state.getSecond();
            lastSymbol = symbol;
            workingStack.push(new Pair<>(lastSymbol, stateIndex));
        } else {
            throw new NullPointerException("Action is SHIFT but there are no matching states");
        }
    }

    private void handleReduceActionInParse(Stack<String> inputStack, Stack<Pair<String, Integer>> workingStack, Stack<String> outputStack, Stack<Integer> outputNumberStack, String lastSymbol, RowTable entry) {
        List<String> reduceContent = new ArrayList<>(entry.reduceContent);

        while (reduceContent.contains(workingStack.peek().getFirst()) && !workingStack.isEmpty()) {
            reduceContent.remove(workingStack.peek().getFirst());
            workingStack.pop();
        }

        Pair<String, Integer> state = parsingTable.entries.get(workingStack.peek().getSecond()).shifts.stream()
                .filter(it -> it.getFirst().equals(entry.reduceNonTerminal)).findAny().orElse(null);

        stateIndex = state.getSecond();
        lastSymbol = entry.reduceNonTerminal;
        workingStack.push(new Pair<>(lastSymbol, stateIndex));

        outputStack.push(entry.reduceProductionString());

        var index = new Pair<>(entry.reduceNonTerminal, entry.reduceContent);
        int productionNumber = this.orderedProductions.indexOf(index);

        outputNumberStack.push(productionNumber);
    }

    private void handleAcceptActionInParse(String filePath, Stack<String> outputStack, Stack<Integer> outputNumberStack) throws IOException {
        List<String> output = new ArrayList<>(outputStack);
        Collections.reverse(output);
        List<Integer> numberOutput = new ArrayList<>(outputNumberStack);
        Collections.reverse(numberOutput);

        System.out.println("ACCEPTED");
        writeToFile(filePath, "ACCEPTED");
        System.out.println("Production strings: " + output);
        writeToFile(filePath, "Production strings: " + output);
        System.out.println("Production number: " + numberOutput);
        writeToFile(filePath, "Production number: " + numberOutput);

        ParserOutput parserOutput = new ParserOutput(grammar);
        parserOutput.generateTreeFromSequence(numberOutput);
        System.out.println("The output tree: ");
        writeToFile(filePath, "The output tree: ");
        parserOutput.printTree(parserOutput.getRoot(), filePath);
    }

    private void handleNullPointerExceptionInParse(int stateIndex, String onErrorSymbol, RowTable lastRow) throws Exception {
        System.out.println("ERROR at state " + stateIndex + " - before symbol " + onErrorSymbol);
        System.out.println(lastRow);
        writeToFile(filePath, "ERROR at state " + stateIndex + " - before symbol " + onErrorSymbol);
        writeToFile(filePath, lastRow.toString());
        throw new Exception("NullPointerException occurred. Parsing halted.");
    }

    public void writeToFile(String file, String line) throws IOException {
        FileWriter fw = new FileWriter(file, true);
        BufferedWriter bw = new BufferedWriter(fw);
        bw.write(line);
        bw.newLine();
        bw.close();
    }

    public Grammar getGrammar() {
        return grammar;
    }

    public Grammar getWorkingGrammar() {
        return workingGrammar;
    }
}
