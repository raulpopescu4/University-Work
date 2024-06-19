package view;

import facade.RestaurantKeeper;
import view.Commands.*;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class View {
    private Map<String, Command> commands = new HashMap<>();
    private RestaurantKeeper keeper;

    private void addCommand(Command c) {
        this.commands.put(c.getKey(), c);
    }

    private void fillCommandsMap() {
        this.addCommand(new GetMenuCommand("1", "Get Menu", keeper));
        this.addCommand(new OrderDishCommand("2", "Order Dish", keeper));
        this.addCommand(new GetCheckCommand("3", "Get Check", keeper));
        this.addCommand(new PayCheckCommand("4", "Pay Check", keeper));
        this.addCommand(new ComposeMealCommand("5", "Compose meal", keeper));
    }

    public View() {
        this.keeper = new RestaurantKeeper();
        this.fillCommandsMap();
    }

    private void printMenu() {
        for(var command: this.commands.values()){
            System.out.println(command.getKey() + " " + command.getDescription());
        }
    }

    public void run() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            printMenu();
            System.out.println("Input the option: ");
            String key = scanner.nextLine();
            Command com = commands.get(key);
            if (com == null){
                System.out.println("Invalid Option");
                continue;
            }
            try {
                com.execute();
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
