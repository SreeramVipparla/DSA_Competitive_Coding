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

public class pattern4 {

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int spaces = 0;
        int stars = n;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= spaces; j++){
                System.out.print("\t");
            }
            for(int j = 1; j <= stars; j++){
                System.out.print("*\t");
            }
            System.out.println();
            spaces++;
            stars--;
        }

    }
}
 /**
 * SOURCE-PEPCODING
 */