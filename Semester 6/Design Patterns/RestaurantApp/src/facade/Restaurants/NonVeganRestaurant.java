package facade.Restaurants;

import domain.Dish;
import facade.Dishes.Dishes;
import facade.Dishes.NonVeganMenu;

import java.util.*;

public class NonVeganRestaurant implements Restaurant {
    List<Dish> dishList = new ArrayList<>();

    @Override
    public Dishes getDishes(){
        initializeMenu();
        return new NonVeganMenu(dishList);
    }

    private void initializeMenu(){
        this.dishList.add(new Dish("Meat Balls", "250kcal/100g", 20, 150));
        this.dishList.add(new Dish("Sushi", "150kcal/100g", 20, 200));
        this.dishList.add(new Dish("Potato chips with chicken strips", "412kcal/100g", 20, 400));

    }
}
