/**
 * QUESTION
1. You are given a number n, representing the number of rows and columns of a square matrix.
2. You are given n * n numbers, representing elements of 2d array a. 
Note - Each row and column is sorted in increasing order.
3. You are given a number x.
4. You are required to find x in the matrix and print it's location int (row, col) format as discussed in output format below.
5. In case element is not found, print "Not Found".
*/


 /**
 * ANSWER
 */
import java.io.*;
import java.util.*;

public class Search_In_A_2D_Sorted_Array {

   public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int n = Integer.parseInt(br.readLine());
      int[][] arr = new int[n][n];

      for (int i = 0; i < n; i++) {
         for (int j = 0; j < n; j++) {
            arr[i][j] = Integer.parseInt(br.readLine());
         }
      }

      int x = Integer.parseInt(br.readLine());

      // search
      int i = 0;
      int j = arr[0].length - 1;
      while(i < arr.length && j >= 0){
         if(x == arr[i][j]){
            System.out.println(i);
            System.out.println(j);
            return;
         } else if(x > arr[i][j]){
            i++;
         } else {
            j--;
         }
      }

      System.out.println("Not Found");
   }


}

 /**
 * SOURCE-PEPCODING
 */