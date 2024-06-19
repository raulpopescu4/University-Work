package decorator;

public class Chicken extends Decorator {

    public Chicken(ICustomMeal customMeal) {
        super(customMeal);
    }

    public String composeMeal() {
        return super.composeMeal() + composeWithChicken();
    }

    private String composeWithChicken() {
        return "with chicken, ";
    }
}
