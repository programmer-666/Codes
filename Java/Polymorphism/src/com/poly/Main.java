package com.poly;

public class Main {

    public static void main(String[] args) {
        /*
        BaseLogger[] bsl = new BaseLogger[]{new DatabaseLogger(), new ioLogger()};
        for(BaseLogger x:bsl){
            x.addLog();
        }*/
        CustomerManager cman = new CustomerManager(new DatabaseLogger());
        cman.addCustomer();
    }
}
