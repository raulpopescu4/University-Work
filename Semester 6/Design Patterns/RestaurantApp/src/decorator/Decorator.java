package decorator;

public abstract class Decorator implements ICustomMeal{

    protected ICustomMeal customMeal;

    public Decorator(ICustomMeal customMeal){
        this.customMeal = customMeal;
    }

    @Override
    public String composeMeal(){
        return customMeal.composeMeal();
    }

}
