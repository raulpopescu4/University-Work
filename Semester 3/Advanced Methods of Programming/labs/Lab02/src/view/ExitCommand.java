package view;

public class ExitCommand extends Command{
    @Override
    public void execute(){
        System.exit(0);
    }

    public ExitCommand(String _key, String _description){
        super(_key, _description);
    }
}
