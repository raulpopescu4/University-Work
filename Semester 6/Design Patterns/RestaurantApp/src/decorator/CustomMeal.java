package decorator;

public class CustomMeal implements ICustomMeal {

    public CustomMeal() {}

    @Override
    public String composeMeal() {
        return "Meal: ";
    }
}
