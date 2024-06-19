package view.Commands;

import facade.RestaurantKeeper;

public abstract class Command {
    private final String key;
    private final String description;

    private final RestaurantKeeper keeper;

    Command(String key, String description, RestaurantKeeper keeper) {
        this.key = key;
        this.description = description;
        this.keeper = keeper;
    }

    public abstract void execute();

    public String getKey() {
        return key;
    }

    public String getDescription() {
        return description;
    }

    public RestaurantKeeper getKeeper(){
        return keeper;
    }
}
