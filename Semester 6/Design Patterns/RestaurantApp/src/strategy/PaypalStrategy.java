package strategy;

public class PaypalStrategy implements PaymentStrategy {

    private final String email;
    private final String password;

    public PaypalStrategy(String email, String password){
        this.email = email;
        this.password = password;
    }

    @Override
    public void pay(long amount) {
        System.out.println(amount + "$ paid using Paypal.");
    }

    public String getEmail() {
        return email;
    }

    public String getPassword() {
        return password;
    }
}
