package strategy;

public class CreditCardStrategy implements PaymentStrategy{
    private final String name;
    private final String cardNumber;
    private final int cvv;
    private final String expirationDate;

    public CreditCardStrategy(String name, String cardNumber, int cvv, String expirationDate) {
        this.name = name;
        this.cardNumber = cardNumber;
        this.cvv = cvv;
        this.expirationDate = expirationDate;
    }

    @Override
    public void pay(long amount) {
        System.out.println(amount + "$ paid with credit card");
    }

    public String getName() {
        return name;
    }

    public String getCardNumber() {
        return cardNumber;
    }

    public int getCvv() {
        return cvv;
    }

    public String getExpirationDate() {
        return expirationDate;
    }
}
