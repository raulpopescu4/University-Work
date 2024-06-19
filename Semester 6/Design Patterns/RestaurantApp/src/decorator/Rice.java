package decorator;

public class Rice extends Decorator {

    public Rice(ICustomMeal customMeal) {
        super(customMeal);
    }

    public String composeMeal() {
        return super.composeMeal() + composeWithRice();
    }

    private String composeWithRice() {
        return "with rice, ";
    }
}
