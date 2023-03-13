package view;

public abstract class Command {

    String key, description;

    public Command(String _key, String _description){
        this.key = _key;
        this.description = _description;
    }

    public String getKey() {
        return key;
    }

    public Object getDescription() {
        return description;
    }

    public abstract void execute();
}
