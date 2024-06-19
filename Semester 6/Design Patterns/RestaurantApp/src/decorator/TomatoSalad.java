package decorator;

public class TomatoSalad extends Decorator {
    public TomatoSalad(ICustomMeal customMeal) {
        super(customMeal);
    }

    public String composeMeal() {
        return super.composeMeal() + composeWithTomatoSalad();
    }

    private String composeWithTomatoSalad() {
        return "with tomato salad, ";
    }
}
