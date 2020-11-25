package com.sstuff;

import javax.management.OperationsException;

public class Main {

    public static void main(String[] args) {
        String opentext = "Lorem ipsum dolor sit amet... ";
        char[] x = new char[5];
        System.out.println(opentext+" "+opentext.length());//length() for strings.
        System.out.println(opentext.charAt(4));
        opentext = opentext.concat("Imperium.. ");
        System.out.println(opentext);
        System.out.println(opentext.startsWith("Lor")+" "+opentext.endsWith(".."));
        opentext.getChars(0, 5, x, 0);//start,end - transferto,start
        System.out.println(x);
        System.out.println(opentext.indexOf('i'));//which char/string in string
        System.out.println(opentext.lastIndexOf('i'));//starts searching from the right side of the string
        // STRINGS #1
        System.out.println(opentext.replace(' ', '-'));
        System.out.println(opentext.substring(0, 5));//first index, last index
        for (String y:opentext.split(" ")) {
            System.out.println(y);
        }
        System.out.println(opentext.toLowerCase().trim()+"\t"+opentext.toUpperCase().trim());
        // STRINGS #2
    }
}
