package com.arrays;

public class Main {
    public static void main(String[] args) {
	    /*String[] vals = new String[3];
        vals[0] = "3f";
        vals[1] = "85";
        vals[2] = "34";
        for(String x:vals){
            System.out.println(x);
        }*/
        //int[][] matris = new int[2][2];
        double[] val = {3.4, 3.14159, 2.44, 21.223, 1.23, 22.0, 1.123};
        double MEM = val[0];
        for (int i = 0; i < val.length; i++){if(val[i]>MEM){MEM=val[i];}}
        System.out.println(MEM);
    }
}
