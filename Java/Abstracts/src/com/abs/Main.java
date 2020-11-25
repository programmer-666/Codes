package com.abs;

public class Main {

    public static void main(String[] args) {
        GameCalculator gameCalculator = new GameCalculator(){public void calc(){System.out.println(1);}};
        // Abstract sınıflar asla new edilemez, zorunlu operasyonlar tanımlanır
        GameCalculator gameCalculator1 = new ChildGameCalculator();
    }
}
