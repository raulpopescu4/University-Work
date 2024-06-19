package view.Commands;

import facade.RestaurantKeeper;

import java.util.Scanner;

public class ComposeMealCommand extends Command {
    public ComposeMealCommand(String key, String description, RestaurantKeeper keeper){
        super(key, description, keeper);
    }

    @Override
    public void execute() {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Below are the available options for composing your own meal: ");
        System.out.println("Choose your first meal component: ");
        System.out.println("1. Rice");
        System.out.println("2. Fries");

        String firstComponent = scanner.nextLine();

        System.out.println("Choose your second meal component: ");

        System.out.println("1. Chicken");
        System.out.println("2. Beef");
        System.out.println("3. Pork");
        System.out.println("4. Falafel");

        String secondComponent = scanner.nextLine();

        System.out.println("Choose the salad you want: ");

        System.out.println("1. Green Salad");
        System.out.println("2. Tomato Salad");

        String saladComponent = scanner.nextLine();

        System.out.println("Choose the topping: ");

        System.out.println("1. Mayonnaise");
        System.out.println("2. Ketchup");

        String toppingComponent = scanner.nextLine();

        this.getKeeper().composeMeal(firstComponent, secondComponent, saladComponent, toppingComponent);

    }
}
