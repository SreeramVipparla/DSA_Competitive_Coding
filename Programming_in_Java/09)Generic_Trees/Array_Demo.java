/**
 * QUESTION

1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a.
4. You are required to display the contents of 2d array as suggested by output format below.
 */


 /**
 * ANSWER
 */
import java.io.*;
import java.util.*;

public class Main{

public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    int m = Integer.parseInt(br.readLine());
    int[][] arr = new int[n][m];

    for(int i = 0; i < n; i++){
       for(int j = 0; j < m; j++){
         arr[i][j] = Integer.parseInt(br.readLine());
       }
    }

    for(int i = 0; i < arr.length; i++){
       for(int j = 0; j < arr[0].length; j++){
          System.out.print(arr[i][j] + " ");
       }
       System.out.println();
    }
 }

}
 /**
 * SOURCE-PEPCODING
 */
