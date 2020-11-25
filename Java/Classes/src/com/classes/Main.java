package com.classes;

public class Main {

    public static void main(String[] args) {
        Management man = new Management(); // referencec
        Management man2 = new Management(); // referencec
        man = man2; // 2 vars 1 heap val
        Management manx = new Management();
        manx.AddJob("Programming");
        manx.ShowJobs();
        manx.FinishJob();
        manx.ShowJobs();
    }
}
