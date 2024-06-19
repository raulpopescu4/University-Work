package decorator;

public class Fries extends Decorator {

    public Fries(ICustomMeal customMeal) {
        super(customMeal);
    }

    public String composeMeal() {
        return super.composeMeal() + composeWithChicken();
    }

    private String composeWithChicken() {
        return "with fries, ";
    }
}
