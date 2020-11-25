package com.methods;

import java.lang.invoke.VarHandle;

public class Main {

    public static void main(String[] args) {
        int[] ar = {1,2,3};
        print(sum(2,3));
        print(len(1,2,3,4));
    }
    public static int sum(int a, int b){return a+b;}
    public static void print(Object x){
        System.out.println(String.valueOf(x));
    }
    public static int len(int... ob){
        return(ob.length); //coverts array
    }
}
