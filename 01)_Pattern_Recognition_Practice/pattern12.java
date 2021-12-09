/**
 * QUESTION

1. You are given a number n.
2. You've to create a pattern of * and separated by tab as shown in output format.

0
1  1
2  3  5
8  13 21  34
 
 
 */


 /**
 * ANSWER
 */

 import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();

        int a = 0;
        int b = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(a + "\t");
                int c = a + b;
                a = b;
                b = c;
            }

            System.out.println();
        }

    }
}
 /**
 * SOURCE-PEPCODING
 */