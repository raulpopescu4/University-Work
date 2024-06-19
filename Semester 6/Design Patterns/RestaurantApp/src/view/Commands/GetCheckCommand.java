package view.Commands;

import facade.RestaurantKeeper;

public class GetCheckCommand extends Command {
    public GetCheckCommand(String key, String description, RestaurantKeeper keeper){
        super(key, description, keeper);
    }

    @Override
    public void execute() {

        System.out.println("Here is the check: " + this.getKeeper().getCheck() + "$");
    }
}
