package decorator;

public class Ketchup extends Decorator{
    public Ketchup(ICustomMeal customMeal) {
        super(customMeal);
    }

    public String composeMeal() {
        return super.composeMeal() + composeWithKetchup();
    }

    private String composeWithKetchup() {
        return "with ketchup as topping.";
    }
}
