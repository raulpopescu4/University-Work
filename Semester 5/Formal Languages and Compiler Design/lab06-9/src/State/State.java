package State;

import java.util.*;
import LR0.Grammar;

/**
 * The state is composed of a set of items (items being of the form [A->alpha.beta])
 */
public class State {

    private StateActionType stateActionType;
    private final Set<Item> items;

    // Constructor
    public State(Set<Item> items) {
        this.items = items;
        setActionForState();
    }

    // Getter methods
    public Set<Item> getItems() {
        return items;
    }

    public StateActionType getStateActionType() {
        return stateActionType;
    }

    public List<String> getSymbolsSucceedingTheDot() {
        Set<String> symbols = new LinkedHashSet<>();

        for (Item item : items) {
            if (item.getPositionForDot() < item.getRightHandSide().size()) {
                symbols.add(item.getRightHandSide().get(item.getPositionForDot()));
            }
        }

        return new ArrayList<>(symbols);
    }

    // Private method to set the action for the state
    private void setActionForState() {
        if (items.size() == 1 && items.iterator().next().getRightHandSide().size() == items.iterator().next().getPositionForDot() &&
                items.iterator().next().getLeftHandSide().equals(Grammar.enrichedStartingGrammarSymbol)) {
            stateActionType = StateActionType.ACCEPT;
        } else if (items.size() == 1 && items.iterator().next().getRightHandSide().size() == items.iterator().next().getPositionForDot()) {
            stateActionType = StateActionType.REDUCE;
        } else if (items.size() >= 1 && items.stream().allMatch(i -> i.getRightHandSide().size() > i.getPositionForDot())) {
            stateActionType = StateActionType.SHIFT;
        } else if (items.size() > 1 && items.stream().allMatch(i -> i.getRightHandSide().size() == i.getPositionForDot())) {
            stateActionType = StateActionType.REDUCE_REDUCE_CONFLICT;
        } else {
            stateActionType = StateActionType.SHIFT_REDUCE_CONFLICT;
        }
    }

    @Override
    public int hashCode() {
        return Objects.hash(items);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof State)) return false;
        State state = (State) obj;
        return Objects.equals(items, state.items);
    }

    @Override
    public String toString() {
        return stateActionType + " - " + items;
    }
}
