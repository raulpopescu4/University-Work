package State;

import java.util.*;

/**
 * An item has the form [A->alpha.beta]
 * Here, the element preceded by the dot is considered to be the element from the dot position.
 * We have a string for the left-hand side, a list of strings for the right-hand side,
 * and the position for the dot.
 */
public class Item {

    private String leftHandSide;
    private List<String> rightHandSide;
    private Integer positionForDot;

    // Constructor
    public Item(String leftHandSide, List<String> rightHandSide, Integer positionForDot) {
        this.leftHandSide = leftHandSide;
        this.rightHandSide = rightHandSide;
        this.positionForDot = positionForDot;
    }

    // Getter methods
    public String getLeftHandSide() {
        return leftHandSide;
    }

    public List<String> getRightHandSide() {
        return rightHandSide;
    }

    public Integer getPositionForDot() {
        return positionForDot;
    }

    public boolean dotIsLast() {
        return positionForDot.equals(rightHandSide.size());
    }

    @Override
    public String toString() {
        List<String> rightHandSide1 = rightHandSide.subList(0, positionForDot);
        String stringRightHandSide1 = String.join("", rightHandSide1);
        List<String> rightHandSide2 = rightHandSide.subList(positionForDot, rightHandSide.size());
        String stringLeftHandSide2 = String.join("", rightHandSide2);
        return leftHandSide + "->" + stringRightHandSide1 + "." + stringLeftHandSide2;
    }

    @Override
    public int hashCode() {
        return Objects.hash(leftHandSide, rightHandSide, positionForDot);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Item)) return false;
        Item item = (Item) obj;
        return Objects.equals(leftHandSide, item.leftHandSide) &&
                Objects.equals(rightHandSide, item.rightHandSide) &&
                Objects.equals(positionForDot, item.positionForDot);
    }
}
