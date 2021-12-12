/**
 * QUESTION

1. You are given a number n1, representing the number of rows of 1st matrix.
2. You are given a number m1, representing the number of columns of 1st matrix.
3. You are given n1*m1 numbers, representing elements of 2d array a1.
4. You are given a number n2, representing the number of rows of 2nd matrix.
5. You are given a number m2, representing the number of columns of 2nd matrix.
6. You are given n2*m2 numbers, representing elements of 2d array a2.
7. If the two arrays representing two matrices of dimensions n1 * m1 and n2 * m2 can be multiplied, display the contents of prd array as specified in output Format.
8. If the two arrays can't be multiplied, print "Invalid input".
 */


 /**
 * ANSWER
 */
import java.io.*;
import java.util.*;

public class Main {

   public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int n1 = Integer.parseInt(br.readLine());
      int m1 = Integer.parseInt(br.readLine());
      int[][] arr1 = new int[n1][m1];

      for (int i = 0; i < n1; i++) {
         for (int j = 0; j < m1; j++) {
            arr1[i][j] = Integer.parseInt(br.readLine());
         }
      }

      int n2 = Integer.parseInt(br.readLine());
      int m2 = Integer.parseInt(br.readLine());
      int[][] arr2 = new int[n2][m2];

      for (int i = 0; i < n2; i++) {
         for (int j = 0; j < m2; j++) {
            arr2[i][j] = Integer.parseInt(br.readLine());
         }
      }

      if (m1 != n2) {
         System.out.println("Invalid input");
         return;
      }

      int[][] prd = new int[n1][m2];
      for (int i = 0; i < n1; i++) {
         for (int j = 0; j < m2; j++) {
            int sum = 0;

            for (int k = 0; k < m1; k++) {
               sum += arr1[i][k] * arr2[k][j];
            }

            prd[i][j] = sum;
         }
      }

      for (int i = 0; i < n1; i++) {
         for (int j = 0; j < m2; j++) {
            System.out.print(prd[i][j] + " ");
         }
         System.out.println();
      }

   }
}
 /**
 * SOURCE-PEPCODING
 */