package com.abs;

public abstract class GameCalculator {
    public abstract void calc(); //soyut
    public final void gameOver(){
        System.out.println("Game Over");
    }
}
