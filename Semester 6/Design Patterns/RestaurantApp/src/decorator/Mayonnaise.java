package decorator;

public class Mayonnaise extends Decorator {

    public Mayonnaise(ICustomMeal customMeal) {
        super(customMeal);
    }

    public String composeMeal() {
        return super.composeMeal() + composeWithMayonnaise();
    }

    private String composeWithMayonnaise() {
        return "with mayonnaise as topping.";
    }
}
