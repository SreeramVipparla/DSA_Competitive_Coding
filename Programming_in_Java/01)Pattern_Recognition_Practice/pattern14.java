/**
 * QUESTION

1. You are given a number n.
2. You've to write code to print it's multiplication table up to 10 in format given below.
 
x * 1 = x
x * 2 = 2x
..
x * 10 = 10x 
 
 */


 /**
 * ANSWER
 */
 import java.util.*;

public class pattern14{

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();

        for (int i = 1; i <= 10; i++) {
            System.out.println(n + " * " + i + " = " + (i * n));
        }

    }
}
 /**
 * SOURCE-PEPCODING
 */