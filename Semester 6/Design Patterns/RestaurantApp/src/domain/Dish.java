package domain;

public class Dish {
    private final String name;
    private final String desc;
    private final long price;
    private final int quantity;


    public Dish(String name, String desc, long price, int quantity) {
        this.name = name;
        this.desc = desc;
        this.price = price;
        this.quantity = quantity;
    }

    public String getName() {
        return name;
    }

    public String getDesc() {
        return desc;
    }

    public long getPrice() {
        return price;
    }

    public int getQuantity() {
        return quantity;
    }
}
