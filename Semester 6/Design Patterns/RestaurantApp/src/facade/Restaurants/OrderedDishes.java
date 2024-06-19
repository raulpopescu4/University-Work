package facade.Restaurants;

import decorator.*;
import facade.Dishes.Ordered;

public class OrderedDishes {
    private long totalPrice;

    public OrderedDishes() {
        this.totalPrice = 0;
    }

    public void addOrderedDish(){
        totalPrice += 20;
    }

    public long getCheck(){
        return totalPrice;
    }

    public void pay(){
        totalPrice = 0;
    }
    public void composeMeal(String firstComponent, String secondComponent, String saladComponent, String toppingComponent){
        ICustomMeal first;

        ICustomMeal second;

        ICustomMeal third;

        ICustomMeal finalMeal;

        switch (firstComponent){
            case "1" -> first = new Rice(new CustomMeal());
            case "2" -> first = new Fries(new CustomMeal());
            default -> first = new CustomMeal();
        }

        switch (secondComponent){
            case "1" -> second = new Chicken(first);
            case "2" -> second = new Beef(first);
            case "3" -> second = new Pork(first);
            case "4" -> second = new Falafel(first);
            default -> second = first;
        }

        switch (secondComponent){
            case "1" -> third = new TomatoSalad(second);
            case "2" -> third = new GreenSalad(second);
            default -> third = first;
        }

        switch (toppingComponent){
            case "1" -> finalMeal = new Mayonnaise(third);
            case "2" -> finalMeal = new Ketchup(third);
            default -> finalMeal = third;
        }

        System.out.println("The meal you composed and ordered: " + finalMeal.composeMeal());
    }
}
