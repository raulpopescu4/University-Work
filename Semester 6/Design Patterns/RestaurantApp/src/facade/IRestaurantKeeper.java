package facade;

import facade.Dishes.NonVeganMenu;
import facade.Dishes.VeganMenu;
import strategy.PaymentStrategy;

public interface IRestaurantKeeper {
    VeganMenu getVeganMenu();
    NonVeganMenu getNonVeganMenu();
    long getCheck();
    void orderDish();
    void setPaymentStrategy(PaymentStrategy strategy);
    void executePaymentStrategy();
    void composeMeal(String firstComponent, String secondComponent, String saladComponent, String toppingComponent);
}
