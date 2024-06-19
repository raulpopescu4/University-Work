package decorator;

public class GreenSalad extends Decorator {

    public GreenSalad(ICustomMeal customMeal) {
        super(customMeal);
    }
    public String composeMeal() {
        return super.composeMeal() + composeWithFalafel();
    }

    private String composeWithFalafel() {
        return "with green salad" +", ";
    }
}
