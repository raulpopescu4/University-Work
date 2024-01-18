package LR0;

import Utils.Pair;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.stream.Collectors;

public class Grammar {

    private final String ELEMENT_SEPARATOR = " ";
    private final String SEPARATOR_OR_TRANSITION = "\\|";
    private final String TRANSITION_CONCATENATION = " ";
    private final String EPSILON = "EPS";
    private final String SEPARATOR_LEFT_RIGHT_HAND_SIDE = "->";

    private Set<String> nonTerminals;
    private Set<String> terminals;
    private Map<List<String>, List<List<String>>> productions;
    private String startingSymbol;
    private boolean isCFG;
    private boolean isEnriched;

    public static String enrichedStartingGrammarSymbol = "S0";

    private void processProduction(String production) {
        String[] leftAndRightHandSide = production.split(this.SEPARATOR_LEFT_RIGHT_HAND_SIDE);
        List<String> splitLHS = List.of(leftAndRightSide[0].split(this.TRANSITION_CONCATENATION));
        String[] splitRHS = leftAndRightSide[1].split(this.SEPARATOR_OR_TRANSITION);

        this.productions.putIfAbsent(splitLHS, new ArrayList<>());
        for (int i = 0; i < splitRHS.length; i++) {
            this.productions.get(splitLHS).add(Arrays.stream(splitRHS[i].split(this.TRANSITION_CONCATENATION)).collect(Collectors.toList()));
        }
    }

    private void loadFromFile(String filePath) {
        try (Scanner scanner = new Scanner(new File(filePath))) {
            this.nonTerminals = new LinkedHashSet<>(List.of(scanner.nextLine().split(this.ELEMENT_SEPARATOR)));
            this.terminals = new LinkedHashSet<>(List.of(scanner.nextLine().split(this.ELEMENT_SEPARATOR)));
            this.startingSymbol = scanner.nextLine();

            this.productions = new LinkedHashMap<>();
            while (scanner.hasNextLine()) {
                this.processProduction(scanner.nextLine());
            }

            this.isCFG = this.checkIfCFG();
            this.isEnriched = false;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    private boolean checkIfCFG() {
        if (!this.nonTerminals.contains(this.startingSymbol)) {
            return false;
        }

        for (List<String> leftHandSide : this.productions.keySet()) {
            if (leftHandSide.size() != 1 || !this.nonTerminals.contains(leftHandSide.get(0))) {
                return false;
            }

            for (List<String> possibleNextMoves : this.productions.get(leftHandSide)) {
                for (String possibleNextMove : possibleNextMoves) {
                    if (!this.nonTerminals.contains(possibleNextMove) && !this.terminals.contains(possibleNextMove) && !possibleNextMove.equals(this.EPSILON)) {
                        return false;
                    }
                }
            }
        }

        return true;
    }

    public Grammar(Set<String> nonTerminals, Set<String> terminals, String startingSymbol, Map<List<String>, List<List<String>>> productions) {
        this.nonTerminals = nonTerminals;
        this.terminals = terminals;
        this.startingSymbol = startingSymbol;
        this.productions = productions;
        this.isEnriched = true;
    }

    public Grammar(String filePath) {
        this.productions = new LinkedHashMap<>();
        this.loadFromFile(filePath);
    }

    public Set<String> getNonTerminals() {
        return this.nonTerminals;
    }

    public Set<String> getTerminals() {
        return this.terminals;
    }

    public Map<List<String>, List<List<String>>> getProductions() {
        return this.productions;
    }

    public String getStartingSymbol() {
        return this.startingSymbol;
    }

    public boolean isCFG() {
        return this.isCFG;
    }

    public Grammar getEnrichedGrammar() throws Exception {
        if (isEnriched) {
            throw new Exception("The LR0.Grammar is already enriched!");
        }

        Grammar enrichedGrammar = new Grammar(nonTerminals, terminals, enrichedStartingGrammarSymbol, productions);

        enrichedGrammar.nonTerminals.add(enrichedStartingGrammarSymbol);
        enrichedGrammar.productions.putIfAbsent(List.of(enrichedStartingGrammarSymbol), new ArrayList<>());
        enrichedGrammar.productions.get(List.of(enrichedStartingGrammarSymbol)).add(List.of(startingSymbol));

        return enrichedGrammar;
    }

    public List<Pair<String, List<String>>> getOrderedProductions() {
        List<Pair<String, List<String>>> result = new ArrayList<>();

        this.productions.forEach(
                (lhs, rhs) -> rhs.forEach(
                        (prod) -> result.add(new Pair<>(lhs.get(0), prod))
                )
        );

        return result;
    }

    public List<List<String>> getProductionsForNonTerminal(String nonTerminal) {
        return getProductions().get(List.of(nonTerminal));
    }
}
