/**
 * QUESTION

1. You are given a number n.
2. You've to create a pattern of * and separated by tab as shown in output format.
 
*  *  *  *  *
*  *  *  *
*  *  *
*  *
*
 
 */


 /**
 * ANSWER
 */
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();

        int nstars = n;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= nstars; j++) {
                System.out.print("*\t");
            }
            nstars--;
            System.out.println();
        }

    }
}
 /**
 * SOURCE-PEPCODING
 */