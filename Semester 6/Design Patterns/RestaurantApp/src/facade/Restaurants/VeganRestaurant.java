package facade.Restaurants;

import domain.Dish;
import facade.Dishes.Dishes;
import facade.Dishes.VeganMenu;

import java.util.*;

public class VeganRestaurant implements Restaurant {

    List<Dish> dishList = new ArrayList<>();


    @Override
    public Dishes getDishes() {
        initializeMenu();
        return new VeganMenu(dishList);
    }

    private void initializeMenu(){
        this.dishList.add(new Dish("Falafel", "150kcal/100g", 20, 150));
        this.dishList.add(new Dish("Unfished fish", "204kcal/100g", 20, 200));
        this.dishList.add(new Dish("Potato chips", "200kcal/100g", 20, 300));

    }

}
