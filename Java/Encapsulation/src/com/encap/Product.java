package com.encap;

public class Product {
// Fields
    private int amount;
    private int id;
    private double price;
    private String name;
    private String description;
// public - open, private - closed / disabled / only inside on defined block
// Fields
// Constructor
    public Product(int id, int amount, double price, String name, String description){
        this.id = id;
        this.amount = amount;
        this.price = price;
        this.name = name;
        this.description = description;
    }
// Constructor
    public int getAmount(){
        return this.amount;
    }
    public int getId(){ // getter
        return this.id;
    }
    public void setId(int id){
        this.id = id;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getCode(){
        return this.name.substring(0,3)+this.id;
    }
}
