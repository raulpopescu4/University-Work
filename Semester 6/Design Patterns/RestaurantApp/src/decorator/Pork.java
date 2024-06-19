package decorator;

public class Pork extends Decorator {
    public Pork(ICustomMeal customMeal) {
        super(customMeal);
    }

    public String composeMeal() {
        return super.composeMeal() + composeWithPork();
    }

    private String composeWithPork() {
        return "with pork";
    }
}
