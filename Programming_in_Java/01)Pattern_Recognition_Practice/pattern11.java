/**
 * QUESTION

1. You are given a number n.
2. You've to create a pattern of * and separated by tab as shown in output format.
 
1
2  3
4  5  6
7  8  9  10
 
 
 */


 /**
 * ANSWER
 */
 import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();

        int val = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(val + "\t");
                val++;
            }

            System.out.println();
        }

    }
}
 /**
 * SOURCE-PEPCODING
 */