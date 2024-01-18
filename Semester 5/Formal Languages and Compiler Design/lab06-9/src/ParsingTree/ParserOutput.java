package ParsingTree;

import LR0.Grammar;
import Utils.Pair;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ParserOutput {

    private ParsingTreeRow root;
    private final Grammar grammar;
    private int currentIndex = 1;
    private int indexInInput = 1;
    private int maxLevel = 0;
    private List<ParsingTreeRow> treeList;

    public ParserOutput(Grammar grammar) {
        this.grammar = grammar;
    }

    public ParsingTreeRow getRoot() {
        return this.root;
    }

    /**
     * With this method, we start the generation of the parse tree
     *
     * @param productionIndices - the list which contains the production numbers (represents actually the output band from the parse algorithm)
     * @return - the root of the tree
     */
    public ParsingTreeRow buildParseTreeFromSequence(List<Integer> productionIndices) {
        int productionIndex = productionIndices.get(0);
        Pair<String, List<String>> productionString = this.grammar.getOrderedProductions().get(productionIndex);
        this.root = new ParsingTreeRow(productionString.getFirst());
        this.root.setIndex(0);
        this.root.setLevel(0);
        this.root.setLeftChild(buildRecursive(1, this.root, productionString.getSecond(), productionIndices));
        return this.root;
    }

    /**
     * With this method, we build recursively each node from the parse tree If it is a terminal, we try to set its right sibling as well If it is a non-terminal, we try to set its right sibling and its left child as well
     *
     * @param level            - the level in the tree
     * @param parent           - the parent of the current node from the tree
     * @param currentContent   - the current elements which compose the production (So if we had A -> a b, then the currentContent is [a, b])
     * @param productionIndices - the list with the production numbers from the output band of the parse algorithm
     * @return - the newly created node
     */
    public ParsingTreeRow buildRecursive(int level, ParsingTreeRow parent, List<String> currentContent, List<Integer> productionIndices) {
        if (currentContent.isEmpty() || this.indexInInput >= productionIndices.size() + 1) {
            return null;
        }

        String currentSymbol = currentContent.get(0);

        if (this.grammar.getTerminals().contains(currentSymbol)) {
            ParsingTreeRow node = new ParsingTreeRow(currentSymbol);
            node.setIndex(this.currentIndex++);
            node.setLevel(level);
            node.setParent(parent);
            List<String> newList = new ArrayList<>(currentContent);
            newList.remove(0);
            node.setRightSibling(buildRecursive(level, parent, newList, productionIndices));
            return node;
        } else if (this.grammar.getNonTerminals().contains(currentSymbol)) {
            int productionIndex = productionIndices.get(this.indexInInput);
            Pair<String, List<String>> productionString = this.grammar.getOrderedProductions().get(productionIndex);
            ParsingTreeRow node = new ParsingTreeRow(currentSymbol);
            node.setIndex(this.currentIndex++);
            node.setLevel(level);
            node.setParent(parent);
            int newLevel = level + 1;
            if (newLevel > this.maxLevel)
                this.maxLevel = newLevel;
            this.indexInInput++;
            node.setLeftChild(buildRecursive(newLevel, node, productionString.getSecond(), productionIndices));
            List<String> newList = new ArrayList<>(currentContent);
            newList.remove(0);
            node.setRightSibling(buildRecursive(level, parent, newList, productionIndices));
            return node;
        } else {
            System.out.println("ERROR");
            return null;
        }
    }

    public void printTree(ParsingTreeRow node, String filePath) throws IOException {
        this.treeList = new ArrayList<>();
        createList(node);
        for (int i = 0; i <= this.maxLevel; i++) {
            for (ParsingTreeRow n : this.treeList) {
                if (n.getLevel() == i) {
                    System.out.println(n);
                    writeToFile(filePath, n.toString());
                }
            }
        }
    }

    public void writeToFile(String file, String line) throws IOException {
        FileWriter fw = new FileWriter(file, true);
        BufferedWriter bw = new BufferedWriter(fw);
        bw.write(line);
        bw.newLine();
        bw.close();
    }

    /**
     * With this method, we compute the order in which the nodes should be in the parsing tree And we effectively create it
     *
     * @param node - the node from which we start the construction (the root in our case)
     */
    public void createList(ParsingTreeRow node) {
        if (node == null)
            return;
        while (node != null) {
            this.treeList.add(node);
            if (node.getLeftChild() != null) {
                createList(node.getLeftChild());
            }
            node = node.getRightSibling();
        }
    }
}
