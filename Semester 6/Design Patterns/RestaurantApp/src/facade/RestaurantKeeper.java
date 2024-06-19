package facade;

import facade.Dishes.NonVeganMenu;
import facade.Dishes.VeganMenu;
import facade.Restaurants.NonVeganRestaurant;
import facade.Restaurants.OrderedDishes;
import facade.Restaurants.VeganRestaurant;
import singleton.Logger;
import strategy.Context;
import strategy.PaymentStrategy;

public class RestaurantKeeper implements IRestaurantKeeper{
    private final VeganRestaurant veganRestaurant;
    private final NonVeganRestaurant nonVeganRestaurant;
    private final OrderedDishes orderedDishes;
    private final Logger logger = Logger.getInstance();
    private Context context;

    public RestaurantKeeper(){
        veganRestaurant = new VeganRestaurant();
        nonVeganRestaurant = new NonVeganRestaurant();
        orderedDishes = new OrderedDishes();
    }

    @Override
    public VeganMenu getVeganMenu() {
        logger.log("HotelKeeperImplementation - Vegan Menu displayed");
        return (VeganMenu) veganRestaurant.getDishes();
    }

    @Override
    public NonVeganMenu getNonVeganMenu() {
        logger.log("HotelKeeperImplementation - Non Vegan Menu displayed ");
        return (NonVeganMenu) nonVeganRestaurant.getDishes();
    }

    @Override
    public long getCheck() {
        logger.log("HotelKeeperImplementation - Check returned");
        return orderedDishes.getCheck();
    }

    @Override
    public void orderDish(){
        logger.log("HotelKeeperImplementation - Dish order to be made");
        this.orderedDishes.addOrderedDish();
        logger.log("HotelKeeperImplementation - Dish ordered");
    }

    @Override
    public void setPaymentStrategy(PaymentStrategy strategy){
        logger.log("HotelKeeperImplementation - payment method to be set");
        this.context = new Context(strategy);
        logger.log("HotelKeeperImplementation - payment method set");
    }

    @Override
    public void executePaymentStrategy(){
        logger.log("HotelKeeperImplementation - payment to be done");
        this.context.pay(getCheck());
        this.orderedDishes.pay();
        logger.log("HotelKeeperImplementation - payment made");
    }

    @Override
    public void composeMeal(String firstComponent, String secondComponent, String saladComponent, String toppingComponent){
        logger.log("HotelKeeperImplementation - Meal to be composed and ordered");
        this.orderedDishes.composeMeal(firstComponent, secondComponent, saladComponent, toppingComponent);
        this.orderDish();
        logger.log("HotelKeeperImplementation - Meal composed and ordered");
    }

}
