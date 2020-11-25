package com.encap;

public class Main {

    public static void main(String[] args) {
        // Attributes
        Product p1 = new Product(1, 1544, 220, "CPU", "Processor for computers.");
        ProductManager prodman = new ProductManager();
        prodman.addProduct(p1);
        //System.out.println(p1.getCode());
        // ürünün özelliklerini ayrı birer değer ile göndermektense sınıfı göndermek daha mantıklıdır
        // refactor>encapsulate fields
        // metotlar overload olduğunda özellikleri birleşir
    }
}
