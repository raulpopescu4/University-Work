package view.Commands;

import facade.RestaurantKeeper;

import java.util.Scanner;

public class OrderDishCommand extends Command {
    public OrderDishCommand(String key, String description, RestaurantKeeper keeper){
        super(key, description, keeper);
    }

    @Override
    public void execute(){

        System.out.println("What dishes would you like to order?");
        Scanner scanner = new Scanner(System.in);
        boolean stillOrdering = true;

        while(stillOrdering){
            String choice = scanner.nextLine();
            if(choice.equals("That's all"))
                stillOrdering = false;
            else if(!choice.equals(""))
                getKeeper().orderDish();
        }

    }
}
