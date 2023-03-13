package view;

import controller.Controller;
import exceptions.MyException;

import java.io.IOException;

public class RunExample extends  Command{
    Controller controller;

    public RunExample(String _key, String _description, Controller _controller){
        super(_key, _description);
        this.controller = _controller;
    }

    @Override
    public void execute(){
        try{
            controller.allStepExecution();
        } catch (MyException | IOException exception){
            System.out.println(exception.getMessage());
        }
    }
}
