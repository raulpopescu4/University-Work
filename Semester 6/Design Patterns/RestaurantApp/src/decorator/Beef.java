package decorator;

public class Beef extends Decorator {

    public Beef(ICustomMeal customMeal) {
        super(customMeal);
    }

    public String composeMeal() {
        return super.composeMeal() + composeWithBeef();
    }

    private String composeWithBeef() {
        return "with beef, ";
    }
}
