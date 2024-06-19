package view.Commands;

import facade.RestaurantKeeper;

import java.util.Scanner;

public class GetMenuCommand extends Command {
    public GetMenuCommand(String key, String description, RestaurantKeeper keeper) {
        super(key, description, keeper);

    }

    @Override
    public void execute() {

        System.out.println("Choose the restaurant: ");
        System.out.println("1. Vegan");
        System.out.println("2. Non Vegan");
        Scanner scanner = new Scanner(System.in);
        String choice = scanner.nextLine();

        switch (choice) {
            case "1" -> System.out.println(this.getKeeper().getVeganMenu().toString());
            case "2" -> System.out.println(this.getKeeper().getNonVeganMenu().toString());
            default -> System.out.println("Invalid option");
        }
    }
}
