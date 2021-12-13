/**
 * QUESTION
1. You are given a square matrix of size 'n'. You are given n*n elements of the square matrix. 
2. You are required to find the saddle price of the given matrix and print the saddle price. 
3. The saddle price is defined as the least price in the row but the maximum price in the column of the matrix.
*/


 /**
 * ANSWER
 */
import java.io.*;
import java.util.*;

public class Main {

   public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int n = Integer.parseInt(br.readLine());
      int[][] arr = new int[n][n];

      for (int i = 0; i < n; i++) {
         for (int j = 0; j < n; j++) {
            arr[i][j] = Integer.parseInt(br.readLine());
         }
      }

      // diagonal traversal
      for(int i = 0; i < arr.length; i++){
         // find min of the row
         int min = arr[i][0];
         int minc = 0;
         for(int j = 1; j < arr[0].length; j++){
            if(arr[i][j] < min){
               min = arr[i][j];
               minc = j;
            }
         }

         // check if no value is higher than this value in it's column
         boolean flag = true;
         for(int k = 0; k < arr.length; k++){
            if(arr[k][minc] > arr[i][minc]){
               flag = false;
               break;
            }
         }

         if(flag == true){
            System.out.println(arr[i][minc]);
            return;
         }
      }

      System.out.println("Invalid input");
   }


}
 /**
 * SOURCE-PEPCODING
 */