package view.Commands;

import facade.RestaurantKeeper;
import strategy.CreditCardStrategy;
import strategy.PaypalStrategy;

import java.util.Scanner;

public class PayCheckCommand extends Command {
    public PayCheckCommand(String key, String description, RestaurantKeeper keeper){
        super(key, description, keeper);
    }

    @Override
    public void execute() {
        System.out.println("Choose the payment method: ");
        System.out.println("1. Credit card");
        System.out.println("2. Paypal");

        Scanner scanner = new Scanner(System.in);
        String choice = scanner.nextLine();

        switch (choice) {
            case "1" ->
            {
                Scanner scannerCard = new Scanner(System.in);
                System.out.println("Please enter the name of the card holder: ");
                String name = scannerCard.nextLine();
                System.out.println("Please enter the card number: ");
                String cardNumber = scannerCard.nextLine();
                System.out.println("Please enter th cvv: ");
                int cvv = scannerCard.nextInt();
                System.out.println("Please enter the expiration date: ");
                String expiryDate = scannerCard.nextLine();

                CreditCardStrategy creditCardStrategy = new CreditCardStrategy(name, cardNumber, cvv, expiryDate);
                this.getKeeper().setPaymentStrategy(creditCardStrategy);
                this.getKeeper().executePaymentStrategy();
            }
            case "2" -> {
                Scanner scannerPayPal = new Scanner(System.in);
                System.out.println("Please enter the email: ");
                String email = scannerPayPal.nextLine();
                System.out.println("Please enter the password: ");
                String password = scannerPayPal.nextLine();


                PaypalStrategy paypalStrategy = new PaypalStrategy(email, password);
                this.getKeeper().setPaymentStrategy(paypalStrategy);
                this.getKeeper().executePaymentStrategy();
            }
            default ->  System.out.println("Invalid option!");

        }
    }
}
