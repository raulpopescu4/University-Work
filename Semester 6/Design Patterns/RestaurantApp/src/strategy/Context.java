package strategy;

public class Context {

    private final PaymentStrategy paymentStrategy;

    public Context(PaymentStrategy paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
    }

    public void pay(long amount) {
        this.paymentStrategy.pay(amount);
    }
}
