package decorator;

public class Falafel extends Decorator {
    public Falafel(ICustomMeal customMeal) {
        super(customMeal);
    }
    public String composeMeal() {
        return super.composeMeal() + composeWithFalafel();
    }

    private String composeWithFalafel() {
        return "with falafel, ";
    }

}
